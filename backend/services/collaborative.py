"""
Collaborative Filtering Recommendation Service (PLACEHOLDER)
==============================================================
TODO: This module is a placeholder for the collaborative filtering team.
      Implement user-item matrix factorization, kNN, or SVD-based
      collaborative filtering here.

Current behaviour: returns a random subset of products as mock data.
"""
import random
from typing import List, Dict, Any
from backend.models.product_data import PRODUCTS


def recommend_collaborative(
    user_id: str,
    num_recommendations: int = 5,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    TODO: Implement collaborative filtering logic.

    Suggested approaches:
      - User-based CF: find similar users, recommend what they liked
      - Item-based CF: find similar items to what user has rated
      - Matrix Factorization (SVD, ALS)
      - Neural Collaborative Filtering

    Current: Returns random products as placeholder.
    """
    # TODO: Replace with actual collaborative filtering implementation
    # TODO: Use user ratings history to find similar users/items
    # TODO: Implement similarity metrics (cosine, pearson, etc.)

    sampled = random.sample(PRODUCTS, min(num_recommendations, len(PRODUCTS)))

    results = []
    for product in sampled:
        results.append({
            "product": product,
            "score": round(random.uniform(3.0, 5.0), 2),
            "explanation": (
                "Recommended based on similar users' preferences. "
                "(Placeholder — collaborative filtering not yet implemented)"
            ),
            "method": "Collaborative Filtering",
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
