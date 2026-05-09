"""
Pydantic schemas for request/response validation.
"""
from pydantic import BaseModel, Field
from typing import Optional, List


# ── Product Schemas ──────────────────────────────────────────────
class ProductOut(BaseModel):
    id: int
    name: str
    category: str
    brand: str
    price: float
    rating: float
    image: str
    description: str
    features: List[str]


# ── User Interaction Schemas ─────────────────────────────────────
class RatingInput(BaseModel):
    user_id: str = Field(..., description="ID of the user submitting the rating")
    product_id: int = Field(..., description="ID of the product being rated")
    rating: float = Field(..., ge=1.0, le=5.0, description="Rating value between 1 and 5")


class RatingOut(BaseModel):
    message: str
    user_id: str
    product_id: int
    rating: float


# ── Recommendation Schemas ───────────────────────────────────────
class RecommendationInput(BaseModel):
    user_id: str = Field(..., description="ID of the user requesting recommendations")
    budget: Optional[float] = Field(None, description="Maximum budget for recommendations")
    category: Optional[str] = Field(None, description="Preferred product category")
    brand: Optional[str] = Field(None, description="Preferred brand")
    min_rating: Optional[float] = Field(None, ge=1.0, le=5.0, description="Minimum acceptable rating")
    preferences: Optional[dict] = Field(default_factory=dict, description="Additional user preferences")
    cf_method: Optional[str] = Field(
        "user_cosine",
        description="Collaborative filtering sub-method: user_cosine, user_pearson, item_cosine, item_jaccard",
    )
    cb_method: Optional[str] = Field(
        "tfidf",
        description="Content-based sub-method: tfidf, lsa, word2vec, feature",
    )


class RecommendedProduct(BaseModel):
    product: ProductOut
    score: float = Field(..., description="Recommendation score")
    explanation: str = Field(..., description="Why this product was recommended")
    method: str = Field(..., description="Which recommendation method was used")


class RecommendationResponse(BaseModel):
    method: str
    user_id: str
    recommendations: List[RecommendedProduct]
    total_results: int
