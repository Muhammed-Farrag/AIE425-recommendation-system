import time
import logging
import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self) -> None:
        """Initialise with empty state. Call load_all() before use."""
        # All attributes start as None — fail loudly if accessed before load_all()
        self.interactions:               pd.DataFrame | None = None
        self.products_features:          pd.DataFrame | None = None
        self.products_text:              pd.DataFrame | None = None
        self.user_products:              dict[str, set[str]] | None = None
        self.user_ratings:               dict[str, dict[str, float]] | None = None
        self.all_product_ids:            np.ndarray | None = None
        self.products_features_indexed:  pd.DataFrame | None = None
        self.products_text_indexed:      pd.DataFrame | None = None
        self._is_loaded:                 bool = False

    def load_all(self) -> None:
        """Load all mock data into memory and build lookup structures."""
        start = time.time()
        self._load_interactions()
        self._load_products_features()
        self._load_products_text()
        elapsed = time.time() - start
        self._is_loaded = True
        logger.info("DataLoader ready in %.2fs — %d products, %d users, %d interactions",
                    elapsed, self.n_products, self.n_users, self.n_interactions)

    def _load_interactions(self) -> None:
        """Build interactions DataFrame from mock user data."""
        from backend.models.user_data import ALL_INTERACTIONS, USER_PRODUCTS, USER_RATINGS

        self.interactions = pd.DataFrame(ALL_INTERACTIONS)
        # user_products and user_ratings are prebuilt in user_data.py for efficiency
        self.user_products = USER_PRODUCTS
        self.user_ratings  = USER_RATINGS
        logger.info("Interactions loaded: %d rows, %d users, %d products",
                    len(self.interactions),
                    self.interactions["user_id"].nunique(),
                    self.interactions["product_id"].nunique())

    def _load_products_features(self) -> None:
        """
        Build products_features DataFrame from mock product data.
        Encodes brand and category fields numerically for FeatureRecommender.
        Normalises price, avg_rating, rating_count to [0, 1].
        """
        from backend.models.product_datar import PRODUCTS, ALL_BRANDS, ALL_CATEGORY_L2, ALL_CATEGORY_L3

        df = pd.DataFrame(PRODUCTS)

        # ── Encode categorical fields to integers ──────────────────────────────
        # LabelEncoding here mirrors what Phase 1 pipeline does with LabelEncoder
        brand_index     = {b: i for i, b in enumerate(ALL_BRANDS)}
        cat_l2_index    = {c: i for i, c in enumerate(ALL_CATEGORY_L2)}
        cat_l3_index    = {c: i for i, c in enumerate(ALL_CATEGORY_L3)}

        df["brand_encoded"]       = df["brand"].map(brand_index).astype(int)
        df["category_l1_encoded"] = 0   # all products are "Electronics" — single value
        df["category_l2_encoded"] = df["category_l2"].map(cat_l2_index).astype(int)
        df["category_l3_encoded"] = df["category_l3"].map(cat_l3_index).astype(int)

        # Keep human-readable names as separate columns for explanations
        df["category_l1_name"] = df["category_l1"]
        df["category_l2_name"] = df["category_l2"]
        df["category_l3_name"] = df["category_l3"]

        # ── Normalise numeric fields to [0, 1] ─────────────────────────────────
        # MinMaxScaler applied per-column; log1p on rating_count to compress outliers
        scaler = MinMaxScaler()
        df["price_norm"]        = scaler.fit_transform(df[["price"]])
        df["avg_rating_norm"]   = scaler.fit_transform(df[["avg_rating"]])
        log1p_counts            = np.log1p(df["rating_count"].values).reshape(-1, 1)
        df["rating_count_norm"] = scaler.fit_transform(log1p_counts)

        # ── Price bucket ───────────────────────────────────────────────────────
        def _bucket(price: float) -> str:
            if price < 30:   return "budget"
            if price < 100:  return "mid-range"
            if price < 300:  return "premium"
            return "luxury"

        BUCKET_ORDER = {"budget": 0, "mid-range": 1, "premium": 2, "luxury": 3}
        df["price_bucket"]         = df["price"].apply(_bucket)
        df["price_bucket_encoded"] = df["price_bucket"].map(BUCKET_ORDER).astype(int)

        # ── Index and canonical ordering ───────────────────────────────────────
        # all_product_ids is the canonical order — ALL matrix row indices use this
        self.all_product_ids            = np.array(sorted(df["product_id"].tolist()))
        df                              = df.set_index("product_id").loc[self.all_product_ids].reset_index()
        self.products_features          = df
        self.products_features_indexed  = df.set_index("product_id")

        logger.info("Products features loaded: %d products, %d columns", *df.shape)

    def _load_products_text(self) -> None:
        """
        Build products_text DataFrame by combining title, brand, description, features.
        full_text is the concatenated, cleaned field consumed by TF-IDF / Word2Vec / LSA.
        """
        from backend.models.product_datar import PRODUCTS

        rows = []
        for p in PRODUCTS:
            # Concatenate all text signals — same formula as Phase 1 pipeline
            raw = (
                f"{p['title']} {p['brand']} "
                f"{p['category_l2']} {p['category_l3']} "
                f"{p['description']} {p.get('features', '')}"
            )
            full_text = self._clean_text(raw)
            rows.append({
                "product_id":  p["product_id"],
                "title":       p["title"],
                "description": p["description"],
                "features":    p.get("features", ""),
                "full_text":   full_text,
                "text_length": len(full_text),
                "token_count": len(full_text.split()),
            })

        df = pd.DataFrame(rows)
        # Align to canonical all_product_ids order — critical for matrix row alignment
        df = df.set_index("product_id").loc[self.all_product_ids].reset_index()
        self.products_text         = df
        self.products_text_indexed = df.set_index("product_id")
        logger.info("Products text loaded: %d rows, avg %.0f tokens/product",
                    len(df), df["token_count"].mean())

    @staticmethod
    def _clean_text(text: str) -> str:
        """Lowercase, strip HTML/URLs, keep alphanumeric + spaces only."""
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"https?://\S+", " ", text)
        text = re.sub(r"[^a-z0-9 ]", " ", text.lower())
        return re.sub(r"\s+", " ", text).strip()

    # ── Public properties ──────────────────────────────────────────────────────

    @property
    def is_loaded(self) -> bool:
        return self._is_loaded

    @property
    def n_users(self) -> int:
        return self.interactions["user_id"].nunique() if self.interactions is not None else 0

    @property
    def n_products(self) -> int:
        return len(self.all_product_ids) if self.all_product_ids is not None else 0

    @property
    def n_interactions(self) -> int:
        return len(self.interactions) if self.interactions is not None else 0

    # ── Data access methods (called by recommenders) ───────────────────────────

    def get_user_positive_products(self, user_id: str, min_rating: float = 3.0) -> list[str]:
        """Return product_ids the user rated >= min_rating. Raises KeyError if user unknown."""
        if user_id not in self.user_ratings:
            raise KeyError(f"User '{user_id}' not found. Available users: U001–U040")
        return [
            pid for pid, rating in self.user_ratings[user_id].items()
            if rating >= min_rating
        ]

    def get_product_info(self, product_id: str) -> dict:
        """Return title, brand, price, price_bucket, category names, avg_rating for one product."""
        if product_id not in self.products_features_indexed.index:
            raise KeyError(f"Product '{product_id}' not found.")
        row = self.products_features_indexed.loc[product_id]
        return {
            "title":            row["title"],
            "brand":            row["brand"],
            "price":            float(row["price"]),
            "price_bucket":     row["price_bucket"],
            "category_l1_name": row["category_l1_name"],
            "category_l2_name": row["category_l2_name"],
            "category_l3_name": row["category_l3_name"],
            "avg_rating":       float(row["avg_rating"]),
            "image":            row["image"],
        }

    def get_texts_in_order(self) -> list[str]:
        """Return full_text values aligned with all_product_ids order. Used by TF-IDF and W2V fit."""
        # Order must match all_product_ids exactly — matrix row i = product all_product_ids[i]
        return self.products_text_indexed.loc[self.all_product_ids, "full_text"].tolist()

    def get_feature_matrix(self) -> np.ndarray:
        """
        Return float32 numpy array of shape (n_products, 8) aligned with all_product_ids.
        Columns: price_norm, avg_rating_norm, rating_count_norm,
                 category_l1_encoded, category_l2_encoded, category_l3_encoded,
                 brand_encoded, price_bucket_encoded
        """
        cols = [
            "price_norm", "avg_rating_norm", "rating_count_norm",
            "category_l1_encoded", "category_l2_encoded", "category_l3_encoded",
            "brand_encoded", "price_bucket_encoded",
        ]
        return (
            self.products_features_indexed
            .loc[self.all_product_ids, cols]
            .to_numpy(dtype=np.float32)
        )

    def validate_consistency(self) -> None:
        """Assert data integrity — called after load_all() to catch corrupt mock data."""
        feat_ids = set(self.products_features["product_id"])
        text_ids = set(self.products_text["product_id"])
        inter_ids = set(self.interactions["product_id"])

        if feat_ids != text_ids:
            raise ValueError(
                f"products_features and products_text have different product sets. "
                f"Diff: {feat_ids.symmetric_difference(text_ids)}"
            )
        orphan_interactions = inter_ids - feat_ids
        if orphan_interactions:
            raise ValueError(
                f"interactions reference {len(orphan_interactions)} unknown product_ids: "
                f"{list(orphan_interactions)[:5]}"
            )
        if self.n_products < 10:
            raise ValueError(f"Too few products ({self.n_products}). Mock data may not have loaded.")
        if self.n_users < 5:
            raise ValueError(f"Too few users ({self.n_users}). Mock data may not have loaded.")
        if self.n_interactions < self.n_products:
            raise ValueError(
                f"Fewer interactions ({self.n_interactions}) than products ({self.n_products}). "
                "Something is wrong with the mock data."
            )
        logger.info("DataLoader consistency check passed ✓")
