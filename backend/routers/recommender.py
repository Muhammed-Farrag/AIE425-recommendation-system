"""
Recommender Router
===================
Main routing hub for all recommendation methods.
Routes requests to the appropriate service based on the method parameter.
"""
from fastapi import APIRouter, HTTPException
from backend.schemas.schemas import RecommendationInput, RecommendationResponse, RecommendedProduct, ProductOut
from backend.services.knowledge_base import (
    recommend_rule_based,
    recommend_constraint_based,
    recommend_utility_based,
)
from backend.services.collaborative import recommend_collaborative
from backend.services.content_based import recommend_content_based

router = APIRouter(prefix="/recommend", tags=["Recommendations"])


def _build_response(method: str, user_id: str, raw_results: list) -> RecommendationResponse:
    """Convert raw service results into a typed response."""
    recommendations = []
    for item in raw_results:
        recommendations.append(
            RecommendedProduct(
                product=ProductOut(**item["product"]),
                score=item["score"],
                explanation=item["explanation"],
                method=item["method"],
            )
        )
    return RecommendationResponse(
        method=method,
        user_id=user_id,
        recommendations=recommendations,
        total_results=len(recommendations),
    )


# ── Compare all knowledge-based methods ──────────────────────────
@router.post("/knowledge-based-compare", response_model=dict)
def compare_knowledge_based(input_data: RecommendationInput):
    """
    Run ALL three knowledge-based methods on the same input
    and return results side-by-side for comparison.
    """
    rule_results = recommend_rule_based(
        budget=input_data.budget,
        category=input_data.category,
        brand=input_data.brand,
        min_rating=input_data.min_rating,
    )
    constraint_results = recommend_constraint_based(
        budget=input_data.budget,
        category=input_data.category,
        brand=input_data.brand,
        min_rating=input_data.min_rating,
        preferences=input_data.preferences,
    )
    utility_results = recommend_utility_based(
        budget=input_data.budget,
        category=input_data.category,
        brand=input_data.brand,
        min_rating=input_data.min_rating,
        preferences=input_data.preferences,
    )

    return {
        "user_id": input_data.user_id,
        "rule_based": _build_response("Knowledge-Based (Rule)", input_data.user_id, rule_results),
        "constraint_based": _build_response("Knowledge-Based (Constraint)", input_data.user_id, constraint_results),
        "utility_based": _build_response("Knowledge-Based (Utility)", input_data.user_id, utility_results),
    }


# ── Knowledge-Based sub-method endpoints ─────────────────────────
@router.post("/knowledge-based/{kb_method}", response_model=RecommendationResponse)
def get_knowledge_based_recommendations(kb_method: str, input_data: RecommendationInput):
    """
    Knowledge-based recommendation with specific method selection.

    Supported kb_methods:
      - rule       → Rule-Based filtering
      - constraint → Constraint-Based (hard + soft constraints)
      - utility    → Utility-Based (weighted scoring)
    """
    if kb_method == "rule":
        results = recommend_rule_based(
            budget=input_data.budget,
            category=input_data.category,
            brand=input_data.brand,
            min_rating=input_data.min_rating,
        )
        return _build_response("Knowledge-Based (Rule)", input_data.user_id, results)

    elif kb_method == "constraint":
        results = recommend_constraint_based(
            budget=input_data.budget,
            category=input_data.category,
            brand=input_data.brand,
            min_rating=input_data.min_rating,
            preferences=input_data.preferences,
        )
        return _build_response("Knowledge-Based (Constraint)", input_data.user_id, results)

    elif kb_method == "utility":
        results = recommend_utility_based(
            budget=input_data.budget,
            category=input_data.category,
            brand=input_data.brand,
            min_rating=input_data.min_rating,
            preferences=input_data.preferences,
        )
        return _build_response("Knowledge-Based (Utility)", input_data.user_id, results)

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown knowledge-based method: '{kb_method}'. Supported: rule, constraint, utility",
        )


# ── General recommendation endpoint ─────────────────────────────
@router.post("/{method}", response_model=RecommendationResponse)
def get_recommendations(method: str, input_data: RecommendationInput):
    """
    General recommendation endpoint.
    Supported methods: collaborative, content-based, knowledge-based
    """
    if method == "collaborative":
        results = recommend_collaborative(
            user_id=input_data.user_id,
        )
        return _build_response("Collaborative Filtering", input_data.user_id, results)

    elif method == "content-based":
        results = recommend_content_based(
            user_id=input_data.user_id,
            category=input_data.category,
        )
        return _build_response("Content-Based", input_data.user_id, results)

    elif method == "knowledge-based":
        # Default to rule-based if no sub-method specified
        results = recommend_rule_based(
            budget=input_data.budget,
            category=input_data.category,
            brand=input_data.brand,
            min_rating=input_data.min_rating,
        )
        return _build_response("Knowledge-Based (Rule)", input_data.user_id, results)

    else:
        raise HTTPException(
            status_code=400,
            detail=f"Unknown method: '{method}'. Supported: collaborative, content-based, knowledge-based",
        )

