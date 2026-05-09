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
from backend.services.collaborative import (
    recommend_collaborative,
    recommend_collaborative_compare,
    CF_METHOD_LABELS,
)

router = APIRouter(prefix="/recommend", tags=["Recommendations"])


# ── Content-based bridge ─────────────────────────────────────────
# The content-based service lives as its own FastAPI sub-app with a
# separate data loader.  We lazily initialise it here so it can be
# called from the unified router like the other services.

_cb_engine = None


def _get_cb_engine():
    """Lazy-init the content-based recommendation engine."""
    global _cb_engine
    if _cb_engine is not None:
        return _cb_engine

    from backend.services.content_based.data_loader import DataLoader
    from backend.services.content_based.tfidf_recommender import TFIDFRecommender
    from backend.services.content_based.lsa_recommender import LSARecommender
    from backend.services.content_based.word2vec_recommender import Word2VecRecommender
    from backend.services.content_based.feature_recommender import FeatureRecommender

    loader = DataLoader()
    loader.load_all()
    loader.validate_consistency()

    recommenders = {}
    recommenders["tfidf"] = TFIDFRecommender(loader)
    recommenders["lsa"] = LSARecommender(loader, recommenders["tfidf"])
    recommenders["word2vec"] = Word2VecRecommender(loader)
    recommenders["feature"] = FeatureRecommender(loader)

    for rec in recommenders.values():
        rec.fit()

    _cb_engine = {"loader": loader, "recommenders": recommenders}
    return _cb_engine


def _recommend_content_based(user_id: str, method: str = "tfidf", k: int = 5):
    """
    Bridge function: calls the content-based sub-engine and maps
    the results into the standard {product, score, explanation, method} format
    expected by _build_response.
    """
    engine = _get_cb_engine()
    loader = engine["loader"]
    recommenders = engine["recommenders"]

    if method not in recommenders:
        raise ValueError(f"Unknown CB method '{method}'. Supported: {list(recommenders.keys())}")

    raw_results = recommenders[method].recommend(user_id, k)

    results = []
    for r in raw_results:
        info = loader.get_product_info(r.product_id)
        # Build a UI-compatible product dict
        product_dict = {
            "id": int(r.product_id[1:]),  # P0001 -> 1
            "name": info["title"],
            "category": info["category_l2_name"],
            "brand": info["brand"],
            "price": info["price"],
            "rating": info["avg_rating"],
            "image": info["image"],
            "description": f"{info['category_l3_name']} in {info['category_l2_name']}",
            "features": [],
        }
        method_label = f"Content-Based ({method.upper()})"
        results.append({
            "product": product_dict,
            "score": round(r.score, 2),
            "explanation": (
                f"Recommended because it matches the content profile of items "
                f"you've rated highly ({method.upper()} similarity)."
            ),
            "method": method_label,
        })

    return results


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


# ── Compare all collaborative filtering methods ──────────────────
@router.post("/collaborative-compare", response_model=dict)
def compare_collaborative(input_data: RecommendationInput):
    """
    Run ALL four CF methods on the same user and return
    results side-by-side for comparison.
    """
    try:
        all_results = recommend_collaborative_compare(user_id=input_data.user_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    response = {"user_id": input_data.user_id}
    for method_key, results in all_results.items():
        label = CF_METHOD_LABELS.get(method_key, method_key)
        response[method_key] = _build_response(label, input_data.user_id, results)
    return response


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
        try:
            results = recommend_collaborative(
                user_id=input_data.user_id,
                cf_method=input_data.cf_method or "user_cosine",
            )
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        label = CF_METHOD_LABELS.get(input_data.cf_method, "Collaborative Filtering")
        return _build_response(label, input_data.user_id, results)

    elif method == "content-based":
        try:
            results = _recommend_content_based(
                user_id=input_data.user_id,
            )
        except (ValueError, KeyError) as e:
            raise HTTPException(status_code=400, detail=str(e))
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
