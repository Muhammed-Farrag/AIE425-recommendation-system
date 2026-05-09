"""
Knowledge-Based Recommendation Service
========================================
Implements three distinct knowledge-based recommendation methods:
  1. Rule-Based
  2. Constraint-Based
  3. Utility-Based

Each method returns different results for the same input by using
different filtering / scoring strategies.
"""
from typing import List, Dict, Any, Optional
from backend.models.product_data import PRODUCTS


def _product_matches_budget(product: dict, budget: Optional[float]) -> bool:
    """Check if product price is within budget."""
    if budget is None:
        return True
    return product["price"] <= budget


def _product_matches_category(product: dict, category: Optional[str]) -> bool:
    """Check if product belongs to the specified category."""
    if category is None:
        return True
    return product["category"].lower() == category.lower()


def _product_matches_brand(product: dict, brand: Optional[str]) -> bool:
    """Check if product belongs to the specified brand."""
    if brand is None:
        return True
    return product["brand"].lower() == brand.lower()


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 1) Rule-Based Method
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def recommend_rule_based(
    budget: Optional[float] = None,
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_rating: Optional[float] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    Rule-Based Recommendation
    --------------------------
    Strict filtering: a product MUST match ALL provided constraints
    to be included. No scoring — order is by rating descending.

    Returns:
        List of recommended products with explanations.
    """
    results = []

    for product in PRODUCTS:
        # Strict match on every provided constraint
        if not _product_matches_budget(product, budget):
            continue
        if not _product_matches_category(product, category):
            continue
        if not _product_matches_brand(product, brand):
            continue
        if min_rating is not None and product["rating"] < min_rating:
            continue

        # Build a human-readable constraint summary
        matched_constraints = []
        if budget is not None:
            matched_constraints.append(f"within ${budget:.0f} budget")
        if category is not None:
            matched_constraints.append(f"category '{category}'")
        if brand is not None:
            matched_constraints.append(f"brand '{brand}'")
        if min_rating is not None:
            matched_constraints.append(f"rating ≥ {min_rating}")

        constraint_text = ", ".join(matched_constraints) if matched_constraints else "no specific constraints"

        results.append({
            "product": product,
            "score": product["rating"],  # score = raw rating (for ordering only)
            "explanation": (
                f"Recommended because it matches your selected constraints: {constraint_text}."
            ),
            "method": "Rule-Based",
        })

    # Sort by rating descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 2) Constraint-Based Method
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def recommend_constraint_based(
    budget: Optional[float] = None,
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_rating: Optional[float] = None,
    preferences: Optional[dict] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    Constraint-Based Recommendation
    --------------------------------
    Separates constraints into:
      • Hard constraints — product MUST satisfy (budget, category)
      • Soft constraints — used for ranking (brand, rating, preferences)

    A simple scoring system ranks products after hard-constraint filtering.

    Returns:
        List of recommended products with explanations.
    """
    if preferences is None:
        preferences = {}

    results = []

    for product in PRODUCTS:
        # ── Hard constraints (must satisfy) ──────────────────────
        if not _product_matches_budget(product, budget):
            continue
        if not _product_matches_category(product, category):
            continue

        # ── Soft constraint scoring ──────────────────────────────
        score = 0.0
        soft_matches = []

        # Brand match (+30 points)
        if brand and _product_matches_brand(product, brand):
            score += 30
            soft_matches.append("brand preference")

        # Rating bonus (0-25 points)
        rating_bonus = (product["rating"] / 5.0) * 25
        score += rating_bonus

        # Min rating soft bonus (+10 if above threshold)
        if min_rating is not None and product["rating"] >= min_rating:
            score += 10
            soft_matches.append(f"rating ≥ {min_rating}")

        # Price efficiency: cheaper relative to budget = higher score
        if budget is not None and budget > 0:
            price_efficiency = ((budget - product["price"]) / budget) * 20
            score += max(price_efficiency, 0)
            soft_matches.append("price efficiency")

        # Feature preferences matching
        preferred_features = preferences.get("features", [])
        if preferred_features:
            matching_features = set(product["features"]) & set(preferred_features)
            feature_score = len(matching_features) * 10
            score += feature_score
            if matching_features:
                soft_matches.append(f"features: {', '.join(matching_features)}")

        soft_text = ", ".join(soft_matches) if soft_matches else "general compatibility"

        results.append({
            "product": product,
            "score": round(score, 2),
            "explanation": (
                f"Recommended because it satisfies your required constraints "
                f"and partially matches your preferences ({soft_text})."
            ),
            "method": "Constraint-Based",
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)
    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 3) Utility-Based Method
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
def recommend_utility_based(
    budget: Optional[float] = None,
    category: Optional[str] = None,
    brand: Optional[str] = None,
    min_rating: Optional[float] = None,
    preferences: Optional[dict] = None,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    Utility-Based Recommendation
    -----------------------------
    Assigns configurable weights to product features and computes
    a utility score for every product (even those outside strict
    constraints), then ranks them.

    Default weights:
      • price_weight   = 0.35  (how well the price fits the budget)
      • rating_weight  = 0.30  (product quality)
      • brand_weight   = 0.20  (brand preference match)
      • feature_weight = 0.15  (feature overlap)

    Returns:
        List of recommended products with explanations.
    """
    if preferences is None:
        preferences = {}

    # Configurable weights (can be passed in preferences)
    w_price   = preferences.get("price_weight", 0.35)
    w_rating  = preferences.get("rating_weight", 0.30)
    w_brand   = preferences.get("brand_weight", 0.20)
    w_feature = preferences.get("feature_weight", 0.15)

    # Normalise weights to sum to 1
    total_w = w_price + w_rating + w_brand + w_feature
    w_price   /= total_w
    w_rating  /= total_w
    w_brand   /= total_w
    w_feature /= total_w

    max_price = max(p["price"] for p in PRODUCTS)
    results = []

    for product in PRODUCTS:
        # Optional: still filter by category if provided
        if category and not _product_matches_category(product, category):
            continue

        score_parts = []

        # ── Price utility ────────────────────────────────────────
        if budget is not None and budget > 0:
            if product["price"] <= budget:
                price_util = 1.0 - (product["price"] / budget)
            else:
                price_util = -0.5  # penalty for over-budget
        else:
            price_util = 1.0 - (product["price"] / max_price)
        score_parts.append(("price", w_price * price_util * 100))

        # ── Rating utility ───────────────────────────────────────
        rating_util = product["rating"] / 5.0
        score_parts.append(("rating", w_rating * rating_util * 100))

        # ── Brand utility ────────────────────────────────────────
        brand_util = 1.0 if (brand and _product_matches_brand(product, brand)) else 0.0
        score_parts.append(("brand", w_brand * brand_util * 100))

        # ── Feature utility ──────────────────────────────────────
        preferred_features = preferences.get("features", [])
        if preferred_features:
            matching = set(product["features"]) & set(preferred_features)
            feature_util = len(matching) / len(preferred_features)
        else:
            feature_util = 0.5  # neutral if no preference
        score_parts.append(("features", w_feature * feature_util * 100))

        total_score = sum(s for _, s in score_parts)

        # Build breakdown text
        breakdown = ", ".join(f"{name}: {val:.1f}" for name, val in score_parts)

        results.append({
            "product": product,
            "score": round(total_score, 2),
            "explanation": (
                f"Recommended based on a weighted match of your preferences "
                f"(utility breakdown: {breakdown})."
            ),
            "method": "Utility-Based",
        })

    # Sort by score descending
    results.sort(key=lambda x: x["score"], reverse=True)

    # Filter out over-budget if budget specified (after ranking, to keep scoring visible)
    if budget is not None:
        results = [r for r in results if r["product"]["price"] <= budget]

    return results
