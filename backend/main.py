"""
FastAPI Main Entry Point
=========================
E-Commerce Intelligent Recommendation System API

Serves as the central hub connecting:
  - Product catalog browsing
  - User ratings & preferences
  - Recommendation engines (Knowledge-Based, Collaborative, Content-Based)
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import products, users, recommender

# ── Application Setup ────────────────────────────────────────────
app = FastAPI(
    title="E-Commerce Recommendation System API",
    description="Intelligent product recommendations using multiple strategies",
    version="1.0.0",
)

# ── CORS (allow frontend dev server) ─────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Register Routers ─────────────────────────────────────────────
app.include_router(products.router)
app.include_router(users.router)
app.include_router(recommender.router)


# ── Health Check ─────────────────────────────────────────────────
@app.get("/", tags=["Health"])
def root():
    return {
        "status": "online",
        "service": "E-Commerce Recommendation System",
        "version": "1.0.0",
        "endpoints": {
            "products": "/products",
            "rate": "/users/rate",
            "recommend": "/recommend/{method}",
            "knowledge_based": "/recommend/knowledge-based/{kb_method}",
            "compare": "/recommend/knowledge-based-compare",
        }
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="0.0.0.0", port=8000, reload=True)
