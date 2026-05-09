import time
import logging
from contextlib import asynccontextmanager
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .data_loader import DataLoader
from .tfidf_recommender import TFIDFRecommender
from .lsa_recommender import LSARecommender
from .word2vec_recommender import Word2VecRecommender
from .feature_recommender import FeatureRecommender

logger = logging.getLogger(__name__)

# Global instances
data_loader = DataLoader()
recommenders = {}
fit_times = {}

@asynccontextmanager
async def lifespan(router: APIRouter):
    """Lifecycle manager: load data and fit models on startup."""
    logger.info("Initializing Content-Based Engine...")
    
    # 1. Load Data
    try:
        data_loader.load_all()
        data_loader.validate_consistency()
    except Exception as e:
        logger.error(f"Failed to load mock data: {e}")
        raise
        
    # 2. Instantiate Recommenders
    recommenders["tfidf"] = TFIDFRecommender(data_loader)
    recommenders["lsa"] = LSARecommender(data_loader, recommenders["tfidf"])
    recommenders["word2vec"] = Word2VecRecommender(data_loader)
    recommenders["feature"] = FeatureRecommender(data_loader)
    
    # 3. Fit Models
    for name, rec in recommenders.items():
        start = time.time()
        try:
            rec.fit()
            fit_times[name] = time.time() - start
            logger.info(f"{name} fitted in {fit_times[name]:.3f}s")
        except Exception as e:
            logger.error(f"Failed to fit {name} recommender: {e}")
            raise

    yield
    
    # Cleanup (if needed)
    logger.info("Shutting down Content-Based Engine.")

api_router = APIRouter(prefix="/api/content-based", tags=["Content-Based Recommendations"])

# Standalone app for isolated testing
from fastapi import FastAPI
router = FastAPI(title="Content-Based Engine API", lifespan=lifespan)

# --- Pydantic Models ---

class RecommendRequest(BaseModel):
    user_id: str
    method: str = "tfidf"  # tfidf, lsa, word2vec, feature
    k: int = 5

class ProductResult(BaseModel):
    product_id: str
    title: str
    brand: str
    price: float
    price_bucket: str
    category_l1_name: str
    category_l2_name: str
    category_l3_name: str
    avg_rating: float
    score: float
    rank: int
    image: str

class RecommendResponse(BaseModel):
    user_id: str
    method: str
    processing_time_ms: float
    recommendations: list[ProductResult]

class CompareResponse(BaseModel):
    user_id: str
    processing_time_ms: float
    results: dict[str, list[ProductResult]]

class HealthResponse(BaseModel):
    status: str
    data_loaded: bool
    n_users: int
    n_products: int
    n_interactions: int
    models_fitted: list[str]

# --- Endpoints ---

@api_router.get("/health", response_model=HealthResponse)
async def health_check():
    return HealthResponse(
        status="ok" if data_loader.is_loaded else "starting",
        data_loaded=data_loader.is_loaded,
        n_users=data_loader.n_users,
        n_products=data_loader.n_products,
        n_interactions=data_loader.n_interactions,
        models_fitted=list(recommenders.keys())
    )

@api_router.get("/fit-info")
async def get_fit_info():
    return {"fit_times_seconds": fit_times}

@api_router.get("/users")
async def get_users():
    if not data_loader.is_loaded:
        raise HTTPException(status_code=503, detail="Engine not ready")
    
    users = []
    # Just list some users or get from user_ratings keys
    for uid in sorted(data_loader.user_ratings.keys()):
        users.append(uid)
    return {"users": users}

@api_router.get("/products/{product_id}")
async def get_product(product_id: str):
    if not data_loader.is_loaded:
        raise HTTPException(status_code=503, detail="Engine not ready")
    
    try:
        return data_loader.get_product_info(product_id)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

def _enrich_results(results: list, method_name: str) -> list[ProductResult]:
    enriched = []
    for r in results:
        info = data_loader.get_product_info(r.product_id)
        enriched.append(ProductResult(
            product_id=r.product_id,
            score=r.score,
            rank=r.rank,
            **info
        ))
    return enriched

@api_router.post("/recommend", response_model=RecommendResponse)
async def recommend(req: RecommendRequest):
    if not data_loader.is_loaded:
        raise HTTPException(status_code=503, detail="Engine not ready")
        
    if req.method not in recommenders:
        raise HTTPException(status_code=400, detail=f"Invalid method. Choose from {list(recommenders.keys())}")
        
    start = time.time()
    try:
        results = recommenders[req.method].recommend(req.user_id, req.k)
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))
        
    enriched = _enrich_results(results, req.method)
    elapsed_ms = (time.time() - start) * 1000
    
    return RecommendResponse(
        user_id=req.user_id,
        method=req.method,
        processing_time_ms=elapsed_ms,
        recommendations=enriched
    )

@api_router.post("/recommend/all", response_model=CompareResponse)
async def recommend_all(req: RecommendRequest):
    if not data_loader.is_loaded:
        raise HTTPException(status_code=503, detail="Engine not ready")
        
    start = time.time()
    all_results = {}
    
    for method_name, rec in recommenders.items():
        try:
            results = rec.recommend(req.user_id, req.k)
            all_results[method_name] = _enrich_results(results, method_name)
        except KeyError as e:
            raise HTTPException(status_code=404, detail=str(e))
            
    elapsed_ms = (time.time() - start) * 1000
    
    return CompareResponse(
        user_id=req.user_id,
        processing_time_ms=elapsed_ms,
        results=all_results
    )

router.include_router(api_router)
