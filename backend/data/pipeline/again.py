"""
phase1_data_foundation.py — Phase 1: Data Foundation Pipeline

Downloads raw Amazon Reviews 2018 Electronics (UCSD, McAuley Lab) via HTTP,
cleans the data, and produces three Parquet tables consumed by all recommender
modules:
  - users_interactions.parquet  (Collaborative Filtering)
  - products_features.parquet   (Content-Based + Knowledge-Based)
  - products_text.parquet       (TF-IDF / Word2Vec / LSA)

Data source:
  Reviews 5-core: http://deepyeti.ucsd.edu/jmcauley/datasets/amazon_v2/
                  categoryFilesSmall/Electronics_5.json.gz
  Metadata:       http://deepyeti.ucsd.edu/jmcauley/datasets/amazon_v2/
                  metaFiles2/meta_Electronics.json.gz

No HuggingFace / datasets library required — stdlib only (urllib + gzip + json).

Run:
  python -m backend.data.pipeline.phase1_data_foundation
"""

from __future__ import annotations

import gc
import gzip
import json
import logging
import math
import pickle
import re
import shutil
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

from backend.data.pipeline.config import (
    CATEGORY_MAX_LEVELS,
    DATA_PROCESSED_DIR,
    DATA_RAW_DIR,
    ENCODERS_FILE,
    FEATURES_FILE,
    INTERACTIONS_FILE,
    KCORE_MAX_ITERATIONS,
    KCORE_MIN_INTERACTIONS,
    METADATA_URL,
    PARQUET_COMPRESSION,
    PARQUET_ENGINE,
    PIPELINE_VERSION,
    PRICE_BUDGET_MAX,
    PRICE_MID_MAX,
    PRICE_PREMIUM_MAX,
    RAW_METADATA_FILENAME,
    RAW_METADATA_PARQUET,
    RAW_REVIEWS_FILENAME,
    RAW_REVIEWS_PARQUET,
    REVIEWS_URL,
    SUMMARY_FILE,
    TEXT_FILE,
    TEXT_MIN_LENGTH,
)

# ---------------------------------------------------------------------------
# Logging setup
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
log = logging.getLogger(__name__)


# ===========================================================================
# STEP 1 — Download (2018 UCSD dataset via HTTP)
# ===========================================================================

def _download_and_parse(
    url: str,
    dest_path: Path,
    parser: Callable[[str], dict | None],
    label: str,
) -> pd.DataFrame:
    """Download a .json.gz from url if absent, then parse each JSONL line."""
    if not dest_path.exists():
        log.info("Downloading %s from %s", label, url)
        try:
            with urllib.request.urlopen(url, timeout=120) as response:
                if response.status != 200:
                    raise ConnectionError(
                        f"HTTP {response.status} downloading {label} from {url}"
                    )
                with open(dest_path, "wb") as f:
                    shutil.copyfileobj(response, f)
            log.info(
                "Downloaded %s → %s (%.1f MB)",
                label, dest_path.name, dest_path.stat().st_size / 1e6,
            )
        except urllib.error.URLError as exc:
            if dest_path.exists():
                dest_path.unlink()  # remove partial file — would silently corrupt next run
            raise ConnectionError(
                f"Cannot reach UCSD servers. Check internet connection.\n"
                f"URL: {url}\nError: {exc}"
            ) from exc
        except Exception as exc:
            if dest_path.exists():
                dest_path.unlink()
            raise RuntimeError(f"Download failed for {label}: {exc}") from exc
    else:
        log.info("%s already downloaded — parsing from %s", label, dest_path.name)

    records: list[dict] = []
    failed_lines = 0
    with gzip.open(dest_path, "rt", encoding="utf-8", errors="replace") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                parsed = parser(line)
                if parsed is not None:
                    records.append(parsed)
            except (json.JSONDecodeError, KeyError, ValueError):
                failed_lines += 1
                if failed_lines <= 5:
                    log.warning("Skipping malformed line %d: %s...", line_number, line[:80])

    if failed_lines > 0:
        log.warning("Skipped %d malformed lines in %s", failed_lines, label)

    if not records:
        raise ValueError(
            f"Parsed 0 records from {label}. "
            "File may be corrupt or schema may have changed."
        )

    df = pd.DataFrame(records)
    log.info("Parsed %s: %d records, %d columns", label, len(df), df.shape[1])
    return df


def _parse_review_line(line: str) -> dict | None:
    """Parse one JSONL line from the 2018 reviews file into a normalised dict."""
    obj = json.loads(line)
    if any(obj.get(field) is None for field in ("reviewerID", "asin", "overall")):
        return None

    # helpful is [upvotes, total_votes]; guard against missing / malformed
    helpful = obj.get("helpful", [0, 0])
    helpful_votes = helpful[0] if isinstance(helpful, list) and len(helpful) > 0 else 0

    return {
        "user_id":           str(obj["reviewerID"]),
        "product_id":        str(obj["asin"]),
        "rating":            float(obj["overall"]),
        "timestamp":         int(obj.get("unixReviewTime", 0)),
        "helpful_votes":     int(helpful_votes),
        "verified_purchase": bool(obj.get("verified", False)),
    }


def _parse_metadata_line(line: str) -> dict | None:
    """
    Parse one JSONL line from the 2018 metadata file.

    Some entries use Python-literal syntax (single quotes) that is not valid
    JSON; these raise JSONDecodeError and are counted as failed lines — that
    is expected (< 1% of records) and acceptable.
    """
    obj = json.loads(line)
    if not obj.get("asin"):
        return None

    # description is a plain string in 2018; occasionally a list — normalise both
    description = obj.get("description", "") or ""
    if isinstance(description, list):
        description = " ".join(str(x) for x in description if x)

    # key is "feature" (singular) in 2018, not "features"
    features_raw = obj.get("feature", []) or []
    if isinstance(features_raw, str):
        features_raw = [features_raw]
    features = " ".join(str(f) for f in features_raw if f)

    # categories: same nested structure [["Electronics", "Headphones", ...]]
    categories_raw = obj.get("categories", [[]]) or [[]]
    categories = categories_raw[0] if categories_raw else []

    return {
        "product_id":  str(obj["asin"]),
        "title":       str(obj.get("title", "") or ""),
        "description": description,
        "features":    features,
        "categories":  categories,
        "brand":       str(obj.get("brand", "") or ""),
        "price":       str(obj.get("price", "") or ""),
    }


def _hf_direct_url(path: str) -> str:
    """Build a direct HuggingFace CDN URL for a dataset file."""
    return (
        "https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023"
        f"/resolve/main/{path}"
    )


def _stream_download(url: str, dest: Path, label: str) -> None:
    """Stream-download url to dest, logging progress every 500 MB."""
    if dest.exists():
        log.info("%s already on disk (%s) — skipping download", label, dest.name)
        return
    log.info("Downloading %s → %s", label, dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=300) as resp:
            chunk_size = 4 * 1024 * 1024   # 4 MB chunks
            downloaded = 0
            with open(dest, "wb") as f:
                while True:
                    chunk = resp.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    downloaded += len(chunk)
                    if downloaded % (500 * 1024 * 1024) < chunk_size:
                        log.info("  %s: %.1f GB downloaded…", label, downloaded / 1e9)
        log.info("Download complete: %s (%.2f GB)", dest.name, dest.stat().st_size / 1e9)
    except Exception as exc:
        if dest.exists():
            dest.unlink()   # remove partial file
        raise RuntimeError(f"Download failed for {label}: {exc}") from exc


def _parse_reviews_jsonl(src: Path) -> pd.DataFrame:
    """
    Parse the Electronics reviews JSONL (2023 HuggingFace schema).
    Fields: user_id, parent_asin, rating, timestamp, helpful_vote, verified_purchase
    """
    records: list[dict] = []
    failed = 0
    log.info("Parsing reviews JSONL: %s", src)
    with gzip.open(src, "rt", encoding="utf-8", errors="replace") if src.suffix == ".gz" \
            else open(src, "r", encoding="utf-8", errors="replace") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
                # 2023 schema: user_id, parent_asin, rating, timestamp, helpful_vote
                uid = obj.get("user_id") or obj.get("reviewerID")
                pid = obj.get("parent_asin") or obj.get("asin")
                rat = obj.get("rating") if obj.get("rating") is not None else obj.get("overall")
                if not uid or not pid or rat is None:
                    continue
                # helpful_vote is an int in 2023; was a [up, total] list in 2018
                hv = obj.get("helpful_vote", 0)
                if isinstance(hv, list):
                    hv = hv[0] if hv else 0
                records.append({
                    "user_id":           str(uid),
                    "product_id":        str(pid),
                    "rating":            float(rat),
                    "timestamp":         int(obj.get("timestamp", obj.get("unixReviewTime", 0))),
                    "helpful_votes":     int(hv or 0),
                    "verified_purchase": bool(obj.get("verified_purchase",
                                                      obj.get("verified", False))),
                })
            except (json.JSONDecodeError, KeyError, ValueError, TypeError):
                failed += 1
                if failed <= 5:
                    log.warning("Malformed review line %d: %s…", lineno, line[:80])
    if failed:
        log.warning("Skipped %d malformed review lines", failed)
    df = pd.DataFrame(records)
    log.info("Parsed reviews: %d rows", len(df))
    return df


def _download_metadata_parquets(dest_dir: Path) -> pd.DataFrame:
    """
    Download the 10 pre-built metadata parquet shards from HuggingFace CDN
    and concatenate them.  Each shard is ~220 MB (2.2 GB total).
    """
    n_shards = 10
    shards: list[pd.DataFrame] = []
    rename = {
        "parent_asin": "product_id",
        "store": "brand",
        "average_rating": "avg_rating",
        "rating_number": "rating_count",
    }
    needed_cols = ["parent_asin", "title", "description", "features",
                   "categories", "store", "price", "average_rating", "rating_number"]

    for i in range(n_shards):
        fname = f"full-{i:05d}-of-{n_shards:05d}.parquet"
        url = _hf_direct_url(f"raw_meta_Electronics/{fname}")
        dest = dest_dir / f"meta_shard_{i:02d}.parquet"
        _stream_download(url, dest, f"metadata shard {i+1}/{n_shards}")
        shard = pd.read_parquet(dest)
        shard = shard[[c for c in needed_cols if c in shard.columns]].rename(columns=rename)
        shards.append(shard)
        log.info("  Shard %d/%d: %d rows", i + 1, n_shards, len(shard))

    df = pd.concat(shards, ignore_index=True)
    log.info("Metadata total: %d rows, %d columns", *df.shape)
    def _safe_str(v: object) -> str:
        """Convert list / numpy array / None / scalar to plain string."""
        if isinstance(v, list):
            return " ".join(str(x) for x in v if x)
        try:
            import numpy as np
            if isinstance(v, np.ndarray):
                return " ".join(str(x) for x in v.tolist() if x)
        except ImportError:
            pass
        return "" if v is None or (hasattr(v, '__len__') and len(v) == 0) else str(v)

    if "description" in df.columns:
        df["description"] = df["description"].apply(_safe_str)
    if "features" in df.columns:
        df["features"] = df["features"].apply(_safe_str)
    return df


def download_or_load_raw() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load Electronics reviews and metadata.  Uses Parquet cache on repeat runs.
    On first run: streams reviews JSONL + metadata parquets directly from
    HuggingFace CDN via urllib — no `datasets` library or script needed.
    Raw files are stored in DATA_RAW_DIR (set HF_DATA_DIR env var to override,
    e.g. point to D: drive when C: is full).
    """
    import os
    raw_dir = Path(os.environ.get("HF_DATA_DIR", str(DATA_RAW_DIR)))
    raw_dir.mkdir(parents=True, exist_ok=True)

    reviews_parquet = raw_dir / RAW_REVIEWS_PARQUET
    metadata_parquet = raw_dir / RAW_METADATA_PARQUET

    if reviews_parquet.exists() and metadata_parquet.exists():
        log.info("Raw Parquet cache found in %s — skipping download", raw_dir)
        reviews_df = pd.read_parquet(reviews_parquet, engine=PARQUET_ENGINE)
        metadata_df = pd.read_parquet(metadata_parquet, engine=PARQUET_ENGINE)
        log.info("Loaded reviews: %s, metadata: %s", reviews_df.shape, metadata_df.shape)
        return reviews_df, metadata_df

    # --- Download reviews JSONL (streamed directly to raw_dir) ---
    reviews_jsonl = raw_dir / "Electronics_reviews.jsonl"
    _stream_download(
        _hf_direct_url("raw/review_categories/Electronics.jsonl"),
        reviews_jsonl,
        "Electronics reviews JSONL",
    )
    reviews_df = _parse_reviews_jsonl(reviews_jsonl)

    # --- Download metadata parquet shards ---
    meta_shard_dir = raw_dir / "meta_shards"
    meta_shard_dir.mkdir(exist_ok=True)
    metadata_df = _download_metadata_parquets(meta_shard_dir)

    # --- Cache as single Parquet files for fast subsequent loads ---
    reviews_df.to_parquet(
        reviews_parquet, engine=PARQUET_ENGINE, compression=PARQUET_COMPRESSION, index=False
    )
    metadata_df.to_parquet(
        metadata_parquet, engine=PARQUET_ENGINE, compression=PARQUET_COMPRESSION, index=False
    )
    log.info("Raw files saved to Parquet cache")
    return reviews_df, metadata_df


# ===========================================================================
# STEP 2 — Merge
# ===========================================================================

def sync_and_validate(
    reviews_df: pd.DataFrame,
    metadata_df: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Keep dataframes separate but ensure they only contain overlapping product_ids.
    If metadata already contains avg_rating / rating_count (2023 HF path), use
    them directly; otherwise compute from reviews (2018 UCSD path).
    """
    log.info(
        "Before sync: reviews=%d rows, metadata=%d rows",
        len(reviews_df), len(metadata_df),
    )

    # Enrich metadata with rating stats only when missing (2018 path)
    if "avg_rating" not in metadata_df.columns or "rating_count" not in metadata_df.columns:
        log.info("Computing avg_rating / rating_count from reviews (not in metadata)")
        rating_stats = (
            reviews_df
            .groupby("product_id")["rating"]
            .agg(avg_rating="mean", rating_count="count")
            .reset_index()
        )
        metadata_df = metadata_df.merge(rating_stats, on="product_id", how="left")
    else:
        log.info("avg_rating / rating_count already in metadata, using as-is")

    # Sync: retain only overlapping products
    valid_products = set(reviews_df["product_id"]).intersection(set(metadata_df["product_id"]))
    
    reviews_df = reviews_df[reviews_df["product_id"].isin(valid_products)]
    metadata_df = metadata_df[metadata_df["product_id"].isin(valid_products)]

    if len(reviews_df) == 0 or len(metadata_df) == 0:
        raise ValueError(
            "Sync produced 0 rows. product_id values may not overlap between "
            "reviews and metadata files. Verify both files are Electronics category."
        )

    log.info(
        "After sync — reviews: %d rows, metadata: %d rows (%d unique products)",
        len(reviews_df),
        len(metadata_df),
        len(valid_products),
    )
    return reviews_df, metadata_df


# ===========================================================================
# STEP 3 — Cleaning pipeline
# ===========================================================================

def _drop_duplicate_interactions(df: pd.DataFrame) -> pd.DataFrame:
    """Keep highest-rated interaction per (user, product) pair."""
    before = len(df)
    df = df.sort_values("rating", ascending=False)
    df = df.drop_duplicates(subset=["user_id", "product_id"], keep="first")
    dropped = before - len(df)
    log.info("Dropped %d duplicate (user, product) pairs", dropped)
    return df


def _drop_products_no_text(df: pd.DataFrame) -> pd.DataFrame:
    """Remove products where title, description, AND features are all empty."""
    def _is_empty(val: Any) -> bool:
        if val is None:
            return True
        if isinstance(val, list):
            return len(val) == 0 or all(str(v).strip() == "" for v in val)
        return str(val).strip() == ""

    mask_no_text = (
        df["title"].apply(_is_empty)
        & df["description"].apply(_is_empty)
        & df["features"].apply(_is_empty)
    )
    before = len(df)
    df = df[~mask_no_text]
    log.info("Dropped %d products with no text content", before - len(df))
    return df


def _parse_price(raw: Any) -> float | None:
    """Strip currency symbols and cast to float; return None on failure."""
    if raw is None or (isinstance(raw, float) and math.isnan(raw)):
        return None
    cleaned = re.sub(r"[^0-9.]", "", str(raw))
    try:
        val = float(cleaned)
        return val if val > 0 else None
    except ValueError:
        return None


def _normalize_price(df: pd.DataFrame) -> pd.DataFrame:
    """
    Parse price strings, fill by brand-level median so that different price
    tiers (e.g. cables vs. TVs) don't distort imputations.
    Brand is used instead of main_category because the 2018 dataset has no
    main_category column; brand is the next-best grouping signal.
    """
    df = df.copy()
    df["price"] = df["price"].apply(_parse_price)

    # Track which rows had no valid price before imputation
    price_was_imputed = df["price"].isnull()

    global_median = df["price"].median()
    # Group by brand; fall back to global median if the whole brand has no prices
    brand_medians = df.groupby("brand")["price"].transform("median")
    fill_values = brand_medians.where(brand_medians.notna(), global_median)
    df["price"] = df["price"].fillna(fill_values)
    df["price_was_imputed"] = price_was_imputed

    imputed_count = int(price_was_imputed.sum())
    pct = 100.0 * imputed_count / len(df)
    log.info("Imputed price for %d products (%.1f%% of catalog)", imputed_count, pct)
    return df


def _normalize_ratings(df: pd.DataFrame) -> pd.DataFrame:
    """Cast rating to float and clip to [1.0, 5.0]."""
    df = df.copy()
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce").clip(1.0, 5.0)
    if df["rating"].isnull().any():
        raise ValueError("Null ratings remain after normalization.")
    return df


def _parse_category_path(raw: Any) -> list[str]:
    """Extract a flat list of category strings from the nested raw field."""
    if raw is None:
        return []
    if isinstance(raw, list):
        # Format: [["Electronics", "Headphones", "Over-Ear"]]
        for item in raw:
            if isinstance(item, list) and len(item) > 0:
                return [str(c).strip() for c in item if str(c).strip()]
            if isinstance(item, str) and item.strip():
                return [item.strip()]
    if isinstance(raw, str) and raw.strip():
        return [raw.strip()]
    return []


def _encode_category_hierarchy(
    df: pd.DataFrame,
) -> tuple[pd.DataFrame, dict[str, LabelEncoder]]:
    """
    Parse categories into up to CATEGORY_MAX_LEVELS levels.
    Missing levels inherit the parent so every product has a full path.
    Encode each level with its own LabelEncoder.
    """
    df = df.copy()
    paths = df["categories"].apply(_parse_category_path)

    for level in range(CATEGORY_MAX_LEVELS):
        col_name = f"category_l{level + 1}_name"
        df[col_name] = paths.apply(
            lambda p, lvl=level: p[lvl] if lvl < len(p) else (p[-1] if p else "Unknown")
        )

    encoders: dict[str, LabelEncoder] = {}
    for level in range(CATEGORY_MAX_LEVELS):
        name_col = f"category_l{level + 1}_name"
        int_col = f"category_l{level + 1}"
        le = LabelEncoder()
        df[int_col] = le.fit_transform(df[name_col].fillna("Unknown"))
        encoders[f"level_{level + 1}"] = le
        log.info("  category_l%d: %d unique values", level + 1, len(le.classes_))

    return df, encoders


def _iterative_kcore(df: pd.DataFrame) -> pd.DataFrame:
    """
    Iteratively remove users and products with fewer than KCORE_MIN_INTERACTIONS
    until the dataset is stable.  One pass can leave orphaned nodes, so we loop.
    """
    k = KCORE_MIN_INTERACTIONS
    for iteration in range(1, KCORE_MAX_ITERATIONS + 1):
        prev_len = len(df)
        user_counts = df["user_id"].value_counts()
        df = df[df["user_id"].isin(user_counts[user_counts >= k].index)]
        product_counts = df["product_id"].value_counts()
        df = df[df["product_id"].isin(product_counts[product_counts >= k].index)]
        log.info(
            "  Iteration %d: %d users, %d products remaining",
            iteration,
            df["user_id"].nunique(),
            df["product_id"].nunique(),
        )
        if len(df) == prev_len:
            break
    else:
        log.warning("k-core reached max iterations (%d) without stabilising.", KCORE_MAX_ITERATIONS)

    log.info(
        "5-core complete: %d users, %d products, %d interactions",
        df["user_id"].nunique(),
        df["product_id"].nunique(),
        len(df),
    )
    return df


def _final_null_audit(df: pd.DataFrame, label: str) -> None:
    """Print null counts for all columns and fail on critical columns."""
    null_counts = df.isnull().sum()
    log.info("%s Null audit:\n%s", label, null_counts.to_string())
    critical = ["user_id", "product_id", "rating", "title"]
    for col in critical:
        if col in df.columns and df[col].isnull().any():
            raise ValueError(f"Critical column '{col}' has nulls in {label} after cleaning.")


def clean(reviews: pd.DataFrame, metadata: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict[str, LabelEncoder]]:
    """Run the full cleaning pipeline and return the cleaned dataframes + encoders."""
    log.info("=== STEP 3: Cleaning pipeline ===")
    reviews = _drop_duplicate_interactions(reviews)
    metadata = _drop_products_no_text(metadata)
    metadata = _normalize_price(metadata)
    reviews = _normalize_ratings(reviews)
    metadata, encoders = _encode_category_hierarchy(metadata)
    
    # Sync after metadata drops to ensure reviews don't keep orphaned items
    valid = set(metadata["product_id"])
    reviews = reviews[reviews["product_id"].isin(valid)]
    
    reviews = _iterative_kcore(reviews)
    
    # Final sync
    valid = set(reviews["product_id"])
    metadata = metadata[metadata["product_id"].isin(valid)]

    _final_null_audit(reviews, "Reviews")
    _final_null_audit(metadata, "Metadata")
    
    if len(reviews) == 0 or len(metadata) == 0:
        raise ValueError("Cleaning pipeline produced 0 rows — aborting.")
    return reviews, metadata, encoders


# ===========================================================================
# STEP 4 — Build derived tables
# ===========================================================================

def _assign_interaction_type(rating: float) -> str:
    if rating >= 4.0:
        return "love"
    if rating == 3.0:
        return "neutral"
    return "dislike"


def build_users_interactions(reviews: pd.DataFrame) -> pd.DataFrame:
    """Primary table for Collaborative Filtering."""
    log.info("=== STEP 4a: Building users_interactions ===")
    cols = ["user_id", "product_id", "rating", "timestamp", "helpful_votes", "verified_purchase"]
    interactions = reviews[cols].copy()

    interactions["helpful_votes"] = interactions["helpful_votes"].fillna(0).astype(int)
    interactions["verified_purchase"] = interactions["verified_purchase"].fillna(False).astype(bool)
    interactions["interaction_type"] = interactions["rating"].apply(_assign_interaction_type).astype("category")
    interactions["days_since_epoch"] = (interactions["timestamp"] / 86400).astype(int)

    interactions = interactions.sort_values(["user_id", "timestamp"]).reset_index(drop=True)

    # Enforce uniqueness on the (user, product) key
    assert interactions.duplicated(subset=["user_id", "product_id"]).sum() == 0, \
        "Duplicate (user_id, product_id) pairs in users_interactions"

    _log_memory(interactions, "users_interactions")
    return interactions


def _assign_price_bucket(price: float) -> str:
    if price < PRICE_BUDGET_MAX:
        return "budget"
    if price < PRICE_MID_MAX:
        return "mid-range"
    if price < PRICE_PREMIUM_MAX:
        return "premium"
    return "luxury"


def build_products_features(
    metadata: pd.DataFrame, interactions: pd.DataFrame
) -> pd.DataFrame:
    """Primary table for Content-Based (structured) and Knowledge-Based."""
    log.info("=== STEP 4b: Building products_features ===")

    # brand, avg_rating, rating_count come from the 2018 parsers/merge;
    # no "store" or pre-computed average_rating in the 2018 schema.
    meta_cols = [
        "product_id", "title", "brand", "price", "price_was_imputed",
        "avg_rating", "rating_count",
        "category_l1", "category_l2", "category_l3",
        "category_l1_name", "category_l2_name", "category_l3_name",
    ]
    features = metadata[meta_cols].drop_duplicates(subset=["product_id"]).copy()
    features["brand"] = features["brand"].fillna("Unknown").astype("category")

    # Fill missing avg_rating from computed mean in interactions
    computed_avg = interactions.groupby("product_id")["rating"].mean().rename("computed_avg")
    features = features.merge(computed_avg, on="product_id", how="left")
    features["avg_rating"] = features["avg_rating"].fillna(features["computed_avg"])
    features = features.drop(columns=["computed_avg"])

    features["rating_count"] = features["rating_count"].fillna(0).astype(int)
    features["price_bucket"] = features["price"].apply(_assign_price_bucket).astype("category")

    scaler = MinMaxScaler()
    features["avg_rating_norm"] = scaler.fit_transform(features[["avg_rating"]].fillna(0))
    log1p_rating = np.log1p(features["rating_count"].values).reshape(-1, 1)
    features["rating_count_norm"] = scaler.fit_transform(log1p_rating)
    features["price_norm"] = scaler.fit_transform(features[["price"]].fillna(0))

    # Low-cardinality string columns as categorical to save RAM
    for col in ["category_l1_name", "category_l2_name", "category_l3_name"]:
        features[col] = features[col].astype("category")

    features = features.reset_index(drop=True)
    _log_memory(features, "products_features")
    return features


def _clean_text(text: str) -> str:
    """
    Normalise text for NLP vectorisation.
    We deliberately keep stopwords — TF-IDF/Word2Vec vectorisers handle that.
    """
    text = re.sub(r"<[^>]+>", " ", text)          # strip HTML tags
    text = re.sub(r"https?://\S+", " ", text)       # remove URLs
    text = re.sub(r"[^a-z0-9 ]", " ", text.lower()) # keep only alphanumeric
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _join_list_field(val: Any) -> str:
    """Flatten a list field to a single string for storage and vectorisation."""
    if isinstance(val, list):
        return " ".join(str(v) for v in val if str(v).strip())
    return str(val) if val is not None else ""


def build_products_text(
    metadata: pd.DataFrame, features: pd.DataFrame
) -> pd.DataFrame:
    """Primary text corpus table for TF-IDF, Word2Vec, LSA."""
    log.info("=== STEP 4c: Building products_text ===")

    # 2018 schema already uses "brand" (not "store"); description and features
    # were normalised to plain strings by _parse_metadata_line.
    text_df = metadata[["product_id", "title", "description", "features", "brand", "category_l1_name", "category_l2_name"]].drop_duplicates(subset=["product_id"]).copy()

    text_df["description"] = text_df["description"].apply(_join_list_field)
    text_df["features"] = text_df["features"].apply(_join_list_field)
    text_df["title"] = text_df["title"].fillna("")
    text_df["brand"] = text_df["brand"].fillna("Unknown")

    # Concatenate all textual signals into one field for vectorisers
    text_df["full_text"] = (
        text_df["title"] + " " + text_df["brand"] + " "
        + text_df["category_l1_name"] + " " + text_df["category_l2_name"] + " "
        + text_df["description"] + " " + text_df["features"]
    ).apply(_clean_text)

    text_df["text_length"] = text_df["full_text"].str.len()
    text_df["token_count"] = text_df["full_text"].str.split().str.len()

    # Restrict to products that are also in products_features (same set)
    valid_ids = set(features["product_id"])
    text_df = text_df[text_df["product_id"].isin(valid_ids)].reset_index(drop=True)

    keep_cols = ["product_id", "title", "description", "features", "full_text",
                 "text_length", "token_count"]
    text_df = text_df[keep_cols]
    _log_memory(text_df, "products_text")
    return text_df


# ===========================================================================
# STEP 5 — Export
# ===========================================================================

def _save_parquet(df: pd.DataFrame, path: Path) -> None:
    """Save a DataFrame as Parquet and verify row count on reload."""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.reset_index(drop=True).to_parquet(
        path, engine=PARQUET_ENGINE, compression=PARQUET_COMPRESSION, index=False
    )
    verify = pd.read_parquet(path)
    assert len(verify) == len(df), (
        f"Verification failed for {path.name}: wrote {len(df)} rows but read {len(verify)}"
    )
    log.info("Saved & verified %s (%d rows)", path.name, len(df))


def _build_summary(
    raw_reviews: pd.DataFrame,
    raw_meta: pd.DataFrame,
    merged: pd.DataFrame,
    interactions: pd.DataFrame,
    features: pd.DataFrame,
) -> dict[str, Any]:
    rating_dist = (
        interactions["rating"].round(0).astype(int).value_counts().sort_index().to_dict()
    )
    price_dist = features["price_bucket"].value_counts().to_dict()
    cat_dist = features["category_l1_name"].value_counts().to_dict()

    return {
        "pipeline_version": PIPELINE_VERSION,
        "run_timestamp": datetime.now(timezone.utc).isoformat(),
        "dataset_source": f"McAuley-Lab/Amazon-Reviews-2018 / Electronics_5.json.gz (UCSD)",
        "raw_reviews_count": len(raw_reviews),
        "raw_products_count": len(raw_meta),
        "after_merge_count": len(merged),
        "after_kcore_users": int(interactions["user_id"].nunique()),
        "after_kcore_products": int(interactions["product_id"].nunique()),
        "after_kcore_interactions": int(len(interactions)),
        "price_imputed_count": int(features["price_was_imputed"].sum()),
        "avg_interactions_per_user": round(
            len(interactions) / interactions["user_id"].nunique(), 2
        ),
        "avg_interactions_per_product": round(
            len(interactions) / interactions["product_id"].nunique(), 2
        ),
        "rating_distribution": {str(k): int(v) for k, v in rating_dist.items()},
        "price_bucket_distribution": {str(k): int(v) for k, v in price_dist.items()},
        "category_l1_distribution": {str(k): int(v) for k, v in cat_dist.items()},
    }


def export_all(
    interactions: pd.DataFrame,
    features: pd.DataFrame,
    text_df: pd.DataFrame,
    encoders: dict[str, LabelEncoder],
    summary: dict[str, Any],
) -> None:
    """Write all processed tables and metadata to DATA_PROCESSED_DIR."""
    DATA_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    _save_parquet(interactions, DATA_PROCESSED_DIR / INTERACTIONS_FILE)
    _save_parquet(features, DATA_PROCESSED_DIR / FEATURES_FILE)
    _save_parquet(text_df, DATA_PROCESSED_DIR / TEXT_FILE)

    enc_path = DATA_PROCESSED_DIR / ENCODERS_FILE
    with open(enc_path, "wb") as f:
        pickle.dump(encoders, f)
    log.info("Saved category encoders → %s", enc_path.name)

    summary_path = DATA_PROCESSED_DIR / SUMMARY_FILE
    with open(summary_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    log.info("Saved data_summary.json")


# ===========================================================================
# Status check (used by FastAPI startup)
# ===========================================================================

def get_pipeline_status() -> dict[str, Any]:
    """
    Check which output files exist and return a status dict.
    FastAPI startup calls this to decide whether to re-run the pipeline.
    """
    expected = [INTERACTIONS_FILE, FEATURES_FILE, TEXT_FILE, ENCODERS_FILE, SUMMARY_FILE]
    present = [f for f in expected if (DATA_PROCESSED_DIR / f).exists()]

    summary: dict[str, Any] = {}
    summary_path = DATA_PROCESSED_DIR / SUMMARY_FILE
    if summary_path.exists():
        with open(summary_path, "r", encoding="utf-8") as fh:
            summary = json.load(fh)

    if len(present) == len(expected):
        status = "complete"
    elif len(present) == 0:
        status = "not_started"
    else:
        status = "partial"

    return {"status": status, "files_present": present, "summary": summary}


# ===========================================================================
# Helpers
# ===========================================================================

def _log_memory(df: pd.DataFrame, label: str) -> None:
    mb = df.memory_usage(deep=True).sum() / 1e6
    log.info("Memory [%s]: %.1f MB", label, mb)


# ===========================================================================
# Orchestrator
# ===========================================================================

def run_pipeline() -> None:
    """Run all five phases in order."""
    log.info("========== Phase 1 Data Foundation Pipeline v%s ==========", PIPELINE_VERSION)

    # Step 1 — download / load from Parquet cache
    raw_reviews, raw_meta = download_or_load_raw()
    raw_reviews_count, raw_meta_count = len(raw_reviews), len(raw_meta)

    # PRE-FILTERING to avoid MemoryError during merge
    log.info("Pre-filtering 21M reviews to k-core before merge to save memory...")
    raw_reviews = _iterative_kcore(raw_reviews)
    surviving_products = raw_reviews["product_id"].unique()
    raw_meta = raw_meta[raw_meta["product_id"].isin(surviving_products)]
    gc.collect()

    # Step 2 — sync
    reviews, metadata = sync_and_validate(raw_reviews, raw_meta)
    after_merge_count = len(reviews)
    del raw_reviews, raw_meta
    gc.collect()

    # Step 3
    reviews, metadata, encoders = clean(reviews, metadata)
    gc.collect()

    # Step 4
    interactions = build_users_interactions(reviews)
    features = build_products_features(metadata, interactions)
    text_df = build_products_text(metadata, features)
    del reviews, metadata
    gc.collect()

    # Rebuild raw counts for summary (we deleted them above — reload summary info)
    summary = _build_summary(
        pd.DataFrame({"_": range(raw_reviews_count)}),
        pd.DataFrame({"_": range(raw_meta_count)}),
        pd.DataFrame({"_": range(after_merge_count)}),
        interactions,
        features,
    )

    # Step 5
    export_all(interactions, features, text_df, encoders, summary)

    log.info("========== Pipeline complete. ==========")
    log.info("Status: %s", get_pipeline_status()["status"])


if __name__ == "__main__":
    run_pipeline()
