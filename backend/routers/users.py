"""
Users Router
=============
Endpoints for user interactions (ratings, preferences).
Uses an in-memory store for simplicity.
"""
from fastapi import APIRouter, HTTPException
from backend.schemas.schemas import RatingInput, RatingOut
from typing import Dict, List

router = APIRouter(prefix="/users", tags=["Users"])

# In-memory stores
# TODO: Replace with actual database integration
user_ratings: Dict[str, List[dict]] = {}
user_preferences: Dict[str, dict] = {}


@router.post("/rate", response_model=RatingOut)
def rate_product(rating_input: RatingInput):
    """
    Submit a rating for a product.
    Stores the rating in-memory for the session.
    """
    user_id = rating_input.user_id

    if user_id not in user_ratings:
        user_ratings[user_id] = []

    # Check if user already rated this product — update if so
    for existing in user_ratings[user_id]:
        if existing["product_id"] == rating_input.product_id:
            existing["rating"] = rating_input.rating
            return RatingOut(
                message="Rating updated successfully",
                user_id=user_id,
                product_id=rating_input.product_id,
                rating=rating_input.rating,
            )

    user_ratings[user_id].append({
        "product_id": rating_input.product_id,
        "rating": rating_input.rating,
    })

    return RatingOut(
        message="Rating submitted successfully",
        user_id=user_id,
        product_id=rating_input.product_id,
        rating=rating_input.rating,
    )


@router.get("/ratings/{user_id}")
def get_user_ratings(user_id: str):
    """Get all ratings submitted by a user."""
    return {"user_id": user_id, "ratings": user_ratings.get(user_id, [])}


@router.post("/preferences/{user_id}")
def set_user_preferences(user_id: str, prefs: dict):
    """
    Save user preferences (category, brand, features, etc.).
    TODO: persist to database.
    """
    user_preferences[user_id] = prefs
    return {"message": "Preferences saved", "user_id": user_id, "preferences": prefs}


@router.get("/preferences/{user_id}")
def get_user_preferences(user_id: str):
    """Retrieve user preferences."""
    return {"user_id": user_id, "preferences": user_preferences.get(user_id, {})}
