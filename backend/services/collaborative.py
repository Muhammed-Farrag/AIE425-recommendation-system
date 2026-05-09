"""
Collaborative Filtering Recommendation Service
=================================================
Implements 4 distinct CF methods using the mock user–item interaction data:

  1. User-Based CF  — Cosine Similarity
  2. User-Based CF  — Pearson Correlation (k-NN, k=5)
  3. Item-Based CF   — Cosine Similarity
  4. Item-Based CF   — Jaccard Similarity (implicit / co-occurrence)

All similarity matrices are computed on-the-fly (40 users × 120 products
is trivially small).  Each method returns a list of dicts compatible with
the ``_build_response`` helper in the recommender router.
"""

from __future__ import annotations

import math
from typing import Any, Dict, List, Optional

from backend.models.product_datar import PRODUCT_BY_ID as ML_PRODUCT_BY_ID
from backend.models.user_data import USER_BY_ID, USER_RATINGS, USER_PRODUCTS, USERS


# ── Mapping helpers ──────────────────────────────────────────────
# The collaborative filtering engine works with the ML product data
# (product_datar.py: P0001…P0120), but the router/frontend expects
# the UI product data (product_data.py: id=1…80).  We map ML product
# IDs to the closest matching UI product by title prefix.

_ML_TO_UI: dict[str, dict | None] = {}


def _get_ui_product(ml_product_id: str) -> Optional[dict]:
    """Return a UI-schema product dict synthesised from the ML product data."""
    if ml_product_id in _ML_TO_UI:
        return _ML_TO_UI[ml_product_id]

    ml_prod = ML_PRODUCT_BY_ID.get(ml_product_id)
    if ml_prod is None:
        _ML_TO_UI[ml_product_id] = None
        return None

    # Synthesize a UI-compatible dict directly from ML data
    # This guarantees a unique mapping for every ML product_id
    ui_dict = {
        "id": int(ml_product_id[1:]),  # P0001 -> 1
        "name": ml_prod["title"],
        "category": ml_prod["category_l2"],
        "brand": ml_prod["brand"],
        "price": ml_prod["price"],
        "rating": ml_prod["avg_rating"],
        "image": ml_prod["image"],
        "description": ml_prod["description"],
        "features": [f.strip() for f in ml_prod.get("features", "").split(",") if f.strip()],
    }

    _ML_TO_UI[ml_product_id] = ui_dict
    return ui_dict


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Similarity functions
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _cosine_similarity(vec_a: dict[str, float], vec_b: dict[str, float]) -> float:
    """Cosine similarity between two sparse rating vectors."""
    common = set(vec_a) & set(vec_b)
    if not common:
        return 0.0
    dot = sum(vec_a[k] * vec_b[k] for k in common)
    mag_a = math.sqrt(sum(v ** 2 for v in vec_a.values()))
    mag_b = math.sqrt(sum(v ** 2 for v in vec_b.values()))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)


def _pearson_correlation(vec_a: dict[str, float], vec_b: dict[str, float]) -> float:
    """Pearson correlation between two sparse rating vectors (mean-centered)."""
    common = set(vec_a) & set(vec_b)
    if len(common) < 2:
        return 0.0

    mean_a = sum(vec_a[k] for k in common) / len(common)
    mean_b = sum(vec_b[k] for k in common) / len(common)

    num = sum((vec_a[k] - mean_a) * (vec_b[k] - mean_b) for k in common)
    den_a = math.sqrt(sum((vec_a[k] - mean_a) ** 2 for k in common))
    den_b = math.sqrt(sum((vec_b[k] - mean_b) ** 2 for k in common))

    if den_a == 0 or den_b == 0:
        return 0.0
    return num / (den_a * den_b)


def _jaccard_similarity(set_a: set[str], set_b: set[str]) -> float:
    """Jaccard index: |intersection| / |union|."""
    if not set_a and not set_b:
        return 0.0
    intersection = set_a & set_b
    union = set_a | set_b
    return len(intersection) / len(union)


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Method 1: User-Based CF — Cosine Similarity
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _user_based_cosine(user_id: str, n: int = 5) -> List[Dict[str, Any]]:
    """
    Find similar users via cosine similarity on their rating vectors,
    then predict scores for unseen items as a weighted average.
    """
    target_ratings = USER_RATINGS[user_id]
    target_products = USER_PRODUCTS[user_id]

    # Compute similarity to every other user
    similarities: list[tuple[str, float]] = []
    for other_id, other_ratings in USER_RATINGS.items():
        if other_id == user_id:
            continue
        sim = _cosine_similarity(target_ratings, other_ratings)
        if sim > 0:
            similarities.append((other_id, sim))

    similarities.sort(key=lambda x: x[1], reverse=True)

    # Predict scores for unseen items
    candidate_scores: dict[str, float] = {}
    candidate_weight: dict[str, float] = {}
    candidate_users: dict[str, list[str]] = {}

    for other_id, sim in similarities:
        other_ratings = USER_RATINGS[other_id]
        for pid, rating in other_ratings.items():
            if pid in target_products:
                continue
            candidate_scores[pid] = candidate_scores.get(pid, 0.0) + sim * rating
            candidate_weight[pid] = candidate_weight.get(pid, 0.0) + sim
            if pid not in candidate_users:
                candidate_users[pid] = []
            candidate_users[pid].append(USER_BY_ID[other_id]["name"])

    # Normalise
    predictions: list[tuple[str, float, list[str]]] = []
    for pid in candidate_scores:
        score = candidate_scores[pid] / candidate_weight[pid] if candidate_weight[pid] > 0 else 0
        predictions.append((pid, score, candidate_users[pid][:3]))

    predictions.sort(key=lambda x: x[1], reverse=True)
    top = predictions[:n]

    results = []
    for pid, score, similar_users in top:
        ui_product = _get_ui_product(pid)
        if ui_product is None:
            continue
        users_text = ", ".join(similar_users)
        results.append({
            "product": ui_product,
            "score": round(score, 2),
            "explanation": (
                f"Recommended because users with similar rating profiles "
                f"(Cosine Similarity) also rated this highly. "
                f"Similar users include: {users_text}."
            ),
            "method": "CF: User-Based Cosine",
        })

    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Method 2: User-Based CF — Pearson Correlation k-NN
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _user_based_pearson_knn(user_id: str, n: int = 5, k: int = 5) -> List[Dict[str, Any]]:
    """
    Pearson-based k-Nearest Neighbours.
    Mean-centres ratings to handle grader bias, then uses only
    the top-k most similar neighbours for prediction.
    """
    target_ratings = USER_RATINGS[user_id]
    target_products = USER_PRODUCTS[user_id]
    target_mean = sum(target_ratings.values()) / len(target_ratings)

    # Compute Pearson similarity to every other user
    similarities: list[tuple[str, float, float]] = []
    for other_id, other_ratings in USER_RATINGS.items():
        if other_id == user_id:
            continue
        sim = _pearson_correlation(target_ratings, other_ratings)
        if sim > 0:
            other_mean = sum(other_ratings.values()) / len(other_ratings)
            similarities.append((other_id, sim, other_mean))

    similarities.sort(key=lambda x: x[1], reverse=True)
    top_k = similarities[:k]

    # Predict scores for unseen items using mean-centred formula
    candidate_num: dict[str, float] = {}
    candidate_den: dict[str, float] = {}
    candidate_users: dict[str, list[str]] = {}

    for other_id, sim, other_mean in top_k:
        other_ratings = USER_RATINGS[other_id]
        for pid, rating in other_ratings.items():
            if pid in target_products:
                continue
            deviation = rating - other_mean
            candidate_num[pid] = candidate_num.get(pid, 0.0) + sim * deviation
            candidate_den[pid] = candidate_den.get(pid, 0.0) + abs(sim)
            if pid not in candidate_users:
                candidate_users[pid] = []
            candidate_users[pid].append(USER_BY_ID[other_id]["name"])

    predictions: list[tuple[str, float, list[str]]] = []
    for pid in candidate_num:
        pred = target_mean + (candidate_num[pid] / candidate_den[pid] if candidate_den[pid] > 0 else 0)
        pred = max(1.0, min(5.0, pred))  # clamp to valid range
        predictions.append((pid, pred, candidate_users[pid][:3]))

    predictions.sort(key=lambda x: x[1], reverse=True)
    top = predictions[:n]

    results = []
    for pid, score, similar_users in top:
        ui_product = _get_ui_product(pid)
        if ui_product is None:
            continue
        users_text = ", ".join(similar_users)
        results.append({
            "product": ui_product,
            "score": round(score, 2),
            "explanation": (
                f"Recommended by your top {k} nearest neighbours who share "
                f"very similar rating behaviours (Pearson Correlation). "
                f"Key neighbours: {users_text}."
            ),
            "method": "CF: User-Based Pearson k-NN",
        })

    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Method 3: Item-Based CF — Cosine Similarity
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _item_based_cosine(user_id: str, n: int = 5) -> List[Dict[str, Any]]:
    """
    Build item–item similarity using cosine on the user-rating vectors,
    then recommend items most similar to those the user liked (≥ 4★).
    """
    target_ratings = USER_RATINGS[user_id]
    target_products = USER_PRODUCTS[user_id]
    liked_items = {pid for pid, r in target_ratings.items() if r >= 4.0}

    # Build item vectors: for each product, its vector is {user_id: rating}
    all_product_ids = set()
    for ur in USER_RATINGS.values():
        all_product_ids.update(ur.keys())

    item_vectors: dict[str, dict[str, float]] = {}
    for uid, ratings in USER_RATINGS.items():
        for pid, rating in ratings.items():
            if pid not in item_vectors:
                item_vectors[pid] = {}
            item_vectors[pid][uid] = rating

    # For each unseen item, compute its max similarity to any liked item
    candidate_scores: dict[str, tuple[float, str]] = {}  # pid -> (best_sim, most_similar_liked_pid)

    unseen = all_product_ids - target_products
    for cand_pid in unseen:
        if cand_pid not in item_vectors:
            continue
        best_sim = 0.0
        best_liked = ""
        for liked_pid in liked_items:
            if liked_pid not in item_vectors:
                continue
            sim = _cosine_similarity(item_vectors[cand_pid], item_vectors[liked_pid])
            if sim > best_sim:
                best_sim = sim
                best_liked = liked_pid
        if best_sim > 0:
            candidate_scores[cand_pid] = (best_sim, best_liked)

    ranked = sorted(candidate_scores.items(), key=lambda x: x[1][0], reverse=True)[:n]

    results = []
    for pid, (sim_score, liked_pid) in ranked:
        ui_product = _get_ui_product(pid)
        if ui_product is None:
            continue
        liked_title = ML_PRODUCT_BY_ID.get(liked_pid, {}).get("title", liked_pid)
        results.append({
            "product": ui_product,
            "score": round(sim_score * 5, 2),  # scale to 0-5 range
            "explanation": (
                f"Recommended because it is frequently highly rated by the same "
                f"users who liked items you enjoy (Item-Based Cosine). "
                f"Most similar to your liked item: \"{liked_title}\"."
            ),
            "method": "CF: Item-Based Cosine",
        })

    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Method 4: Item-Based CF — Jaccard Similarity (Implicit Feedback)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def _item_based_jaccard(user_id: str, n: int = 5) -> List[Dict[str, Any]]:
    """
    Convert ratings to implicit interactions (rating ≥ 3 = interacted),
    then use Jaccard Index to find similar items based on user overlap.
    """
    target_ratings = USER_RATINGS[user_id]
    target_products = USER_PRODUCTS[user_id]
    liked_items = {pid for pid, r in target_ratings.items() if r >= 3.0}

    # Build implicit item sets: for each product, the set of users who interacted
    item_user_sets: dict[str, set[str]] = {}
    for uid, ratings in USER_RATINGS.items():
        for pid, rating in ratings.items():
            if rating >= 3.0:
                if pid not in item_user_sets:
                    item_user_sets[pid] = set()
                item_user_sets[pid].add(uid)

    # Collect all product IDs
    all_product_ids = set()
    for ur in USER_RATINGS.values():
        all_product_ids.update(ur.keys())

    # For each unseen item, compute avg Jaccard similarity to liked items
    candidate_scores: dict[str, tuple[float, str]] = {}

    unseen = all_product_ids - target_products
    for cand_pid in unseen:
        if cand_pid not in item_user_sets:
            continue
        best_sim = 0.0
        best_liked = ""
        for liked_pid in liked_items:
            if liked_pid not in item_user_sets:
                continue
            sim = _jaccard_similarity(item_user_sets[cand_pid], item_user_sets[liked_pid])
            if sim > best_sim:
                best_sim = sim
                best_liked = liked_pid
        if best_sim > 0:
            candidate_scores[cand_pid] = (best_sim, best_liked)

    ranked = sorted(candidate_scores.items(), key=lambda x: x[1][0], reverse=True)[:n]

    results = []
    for pid, (sim_score, liked_pid) in ranked:
        ui_product = _get_ui_product(pid)
        if ui_product is None:
            continue
        liked_title = ML_PRODUCT_BY_ID.get(liked_pid, {}).get("title", liked_pid)
        results.append({
            "product": ui_product,
            "score": round(sim_score * 5, 2),  # scale to 0-5 range
            "explanation": (
                f"Recommended because users who interact with your favourite items "
                f"also frequently interact with this (Jaccard Similarity on implicit feedback). "
                f"Most similar to your item: \"{liked_title}\"."
            ),
            "method": "CF: Item-Based Jaccard",
        })

    return results


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Public API — used by the router
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CF_METHODS = {
    "user_cosine":  _user_based_cosine,
    "user_pearson": _user_based_pearson_knn,
    "item_cosine":  _item_based_cosine,
    "item_jaccard": _item_based_jaccard,
}

CF_METHOD_LABELS = {
    "user_cosine":  "CF: User-Based Cosine",
    "user_pearson": "CF: User-Based Pearson k-NN",
    "item_cosine":  "CF: Item-Based Cosine",
    "item_jaccard": "CF: Item-Based Jaccard",
}


def recommend_collaborative(
    user_id: str,
    cf_method: str = "user_cosine",
    num_recommendations: int = 5,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    Main entry point for collaborative filtering.

    Parameters
    ----------
    user_id : str
        Target user (e.g. "U001").
    cf_method : str
        One of: user_cosine, user_pearson, item_cosine, item_jaccard.
    num_recommendations : int
        How many items to return.

    Returns
    -------
    list[dict]
        Each dict has keys: product, score, explanation, method.
    """
    if user_id not in USER_BY_ID:
        raise ValueError(f"User '{user_id}' not found. Available: U001–U040")

    fn = CF_METHODS.get(cf_method)
    if fn is None:
        raise ValueError(
            f"Unknown CF method '{cf_method}'. "
            f"Supported: {', '.join(CF_METHODS.keys())}"
        )

    return fn(user_id, num_recommendations)


def recommend_collaborative_compare(
    user_id: str,
    num_recommendations: int = 5,
) -> Dict[str, List[Dict[str, Any]]]:
    """Run all 4 CF methods and return results keyed by method name."""
    if user_id not in USER_BY_ID:
        raise ValueError(f"User '{user_id}' not found. Available: U001–U040")

    return {
        method_key: fn(user_id, num_recommendations)
        for method_key, fn in CF_METHODS.items()
    }
