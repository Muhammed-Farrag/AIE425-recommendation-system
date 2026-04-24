"""
Intelligent E-commerce Recommender System
FastAPI Backend - Main Entry Point
"""

from fastapi import FastAPI, HTTPException, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import List, Optional
import os
import json
from pathlib import Path

# Import recommendation algorithms
from algorithms.collaborative_filtering import CollaborativeFiltering
from algorithms.content_based import ContentBased
from algorithms.knowledge_based import KnowledgeBased
from algorithms.data_manager import DataManager

# ============ FastAPI Setup ============
app = FastAPI(
    title="Intelligent E-commerce Recommender System",
    description="A comprehensive recommender system with multiple approaches",
    version="1.0.0"
)

# Mount static files (CSS, JS, Images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ============ Data Models ============
class User(BaseModel):
    id: Optional[int] = None
    name: str
    preferences: List[str]
    budget: float

class Product(BaseModel):
    id: int
    name: str
    category: str
    price: float
    brand: str
    rating: float
    description: str
    tags: List[str]

class Recommendation(BaseModel):
    productId: int
    score: float
    reason: str
    method: str

class RecommendationResponse(BaseModel):
    collaborativeFiltering: List[Recommendation]
    contentBased: List[Recommendation]
    knowledgeBased: List[Recommendation]

class AnalysisMetrics(BaseModel):
    method: str
    precision: float
    recall: float
    rmse: float
    coverage: float

# ============ Initialize Managers ============
data_manager = DataManager()
cf_engine = CollaborativeFiltering(data_manager)
cb_engine = ContentBased(data_manager)
kb_engine = KnowledgeBased(data_manager)

# ============ Routes - HTML Pages ============
@app.get("/")
async def root():
    """Serve the main index.html page"""
    return FileResponse("templates/index.html")

@app.get("/recommendations")
async def recommendations_page():
    """Serve recommendations page"""
    return FileResponse("templates/recommendations.html")

@app.get("/analysis")
async def analysis_page():
    """Serve analysis page"""
    return FileResponse("templates/analysis.html")

@app.get("/custom")
async def custom_page():
    """Serve custom recommendations page"""
    return FileResponse("templates/custom.html")

@app.get("/add-user")
async def add_user_page():
    """Serve add user page"""
    return FileResponse("templates/add_user.html")

# ============ API Routes - Data ============

@app.get("/api/users", response_model=List[dict])
async def get_users():
    """Get all users"""
    try:
        users = data_manager.get_all_users()
        return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/products", response_model=List[dict])
async def get_products():
    """Get all products"""
    try:
        products = data_manager.get_all_products()
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/products/category/{category}")
async def get_products_by_category(category: str):
    """Get products by category"""
    try:
        products = data_manager.get_products_by_category(category)
        return products
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/users")
async def add_user(
    name: str = Form(...),
    preferences: str = Form(...),
    budget: float = Form(...)
):
    """Add a new user to the system"""
    try:
        # Parse preferences (comma-separated)
        preference_list = [pref.strip() for pref in preferences.split(",")]
        
        # Add user to data manager
        new_user = data_manager.add_user(name, preference_list, budget)
        
        return {
            "success": True,
            "message": f"User '{name}' added successfully!",
            "user": new_user
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ API Routes - Recommendations ============

@app.post("/api/recommendations/{user_id}", response_model=RecommendationResponse)
async def get_recommendations(user_id: int):
    """Get recommendations for a user using all three methods"""
    try:
        # Get recommendations from all three methods
        cf_recs = cf_engine.recommend(user_id)
        cb_recs = cb_engine.recommend(user_id)
        kb_recs = kb_engine.recommend(user_id)
        
        return RecommendationResponse(
            collaborativeFiltering=cf_recs,
            contentBased=cb_recs,
            knowledgeBased=kb_recs
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/recommendations/custom")
async def get_custom_recommendations(
    name: str = Form(...),
    categories: str = Form(...),
    budget: float = Form(...)
):
    """Get recommendations for a custom user"""
    try:
        # Parse categories (comma-separated)
        category_list = [cat.strip() for cat in categories.split(",")]
        
        # Create temporary user
        temp_user = {
            "name": name,
            "categories": category_list,
            "budget": budget
        }
        
        # Get recommendations
        cf_recs = cf_engine.recommend_custom(temp_user)
        cb_recs = cb_engine.recommend_custom(temp_user)
        kb_recs = kb_engine.recommend_custom(temp_user)
        
        return {
            "collaborativeFiltering": cf_recs,
            "contentBased": cb_recs,
            "knowledgeBased": kb_recs
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ API Routes - Analysis ============

@app.get("/api/analysis/metrics")
async def get_analysis_metrics():
    """Get evaluation metrics for all methods"""
    try:
        metrics = {
            "collaborativeFiltering": cf_engine.get_metrics(),
            "contentBased": cb_engine.get_metrics(),
            "knowledgeBased": kb_engine.get_metrics()
        }
        return metrics
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/analysis/comparison")
async def get_comparison():
    """Get comparison data for visualization"""
    try:
        comparison = {
            "cf": cf_engine.get_metrics(),
            "cb": cb_engine.get_metrics(),
            "kb": kb_engine.get_metrics()
        }
        return comparison
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ============ Health Check ============

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Intelligent E-commerce Recommender System",
        "version": "1.0.0"
    }

# ============ Error Handlers ============

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    """Handle HTTP exceptions"""
    return {
        "error": exc.detail,
        "status_code": exc.status_code
    }

# ============ Main Entry Point ============

if __name__ == "__main__":
    import uvicorn
    
    # Run the server
    # Host: 0.0.0.0 (accessible from any IP)
    # Port: 8000 (default FastAPI port)
    # Reload: True (auto-reload on code changes)
    uvicorn.run(
        "app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
