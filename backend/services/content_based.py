"""
Content-Based Recommendation Service (PLACEHOLDER)
====================================================
TODO: This module is a placeholder for the content-based team.
      Implement TF-IDF, word embeddings, or feature similarity
      approaches here.

Current behaviour: returns products from the same category as mock data.
"""
import random
from typing import List, Dict, Any, Optional
from backend.models.product_data import PRODUCTS


def recommend_content_based(
    user_id: str,
    category: Optional[str] = None,
    num_recommendations: int = 5,
    **kwargs,
) -> List[Dict[str, Any]]:
    """
    TODO: Implement content-based filtering logic.

    Suggested approaches:
      - TF-IDF on product descriptions
      - Word2Vec / Doc2Vec embeddings
      - Feature vector cosine similarity
      - Tag / attribute matching

    Current: Returns products from the same category as placeholder.
    """
    # TODO: Replace with actual content-based implementation
    # TODO: Build product feature vectors from descriptions
    # TODO: Compute similarity between user profile and product features
    # TODO: Use NLP to extract keywords from product descriptions

    if category:
        filtered = [p for p in PRODUCTS if p["category"].lower() == category.lower()]
    else:
        filtered = PRODUCTS.copy()

    sampled = random.sample(filtered, min(num_recommendations, len(filtered)))

    results = []
    for product in sampled:
        results.append({
            "product": product,
            "score": round(random.uniform(3.0, 5.0), 2),
            "explanation": (
                f"Recommended because it shares features with products you've liked. "
                f"(Placeholder — content-based filtering not yet implemented)"
            ),
            "method": "Content-Based",
        })

    results.sort(key=lambda x: x["score"], reverse=True)
    return results
