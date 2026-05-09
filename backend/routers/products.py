"""
Products Router
================
Endpoints for browsing and filtering the product catalog.
"""
from fastapi import APIRouter, Query
from typing import Optional, List
from backend.models.product_data import PRODUCTS, CATEGORIES, BRANDS
from backend.schemas.schemas import ProductOut

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=List[ProductOut])
def get_products(
    category: Optional[str] = Query(None, description="Filter by category"),
    brand: Optional[str] = Query(None, description="Filter by brand"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price"),
    min_rating: Optional[float] = Query(None, ge=1, le=5, description="Minimum rating"),
    search: Optional[str] = Query(None, description="Search in product name/description"),
    sort_by: Optional[str] = Query("rating", description="Sort by: price, rating, name"),
    order: Optional[str] = Query("desc", description="Sort order: asc, desc"),
):
    """
    Retrieve products with optional filters, search, and sorting.
    """
    filtered = PRODUCTS.copy()

    # Apply filters
    if category:
        filtered = [p for p in filtered if p["category"].lower() == category.lower()]
    if brand:
        filtered = [p for p in filtered if p["brand"].lower() == brand.lower()]
    if min_price is not None:
        filtered = [p for p in filtered if p["price"] >= min_price]
    if max_price is not None:
        filtered = [p for p in filtered if p["price"] <= max_price]
    if min_rating is not None:
        filtered = [p for p in filtered if p["rating"] >= min_rating]
    if search:
        search_lower = search.lower()
        filtered = [
            p for p in filtered
            if search_lower in p["name"].lower() or search_lower in p["description"].lower()
        ]

    # Sorting
    reverse = order != "asc"
    if sort_by == "price":
        filtered.sort(key=lambda p: p["price"], reverse=reverse)
    elif sort_by == "name":
        filtered.sort(key=lambda p: p["name"].lower(), reverse=reverse)
    else:
        filtered.sort(key=lambda p: p["rating"], reverse=reverse)

    return filtered


@router.get("/{product_id}", response_model=ProductOut)
def get_product_by_id(product_id: int):
    """Retrieve a single product by its ID."""
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Product not found")


@router.get("/meta/categories")
def get_categories():
    """Return the list of available product categories."""
    return {"categories": sorted(CATEGORIES)}


@router.get("/meta/brands")
def get_brands():
    """Return the list of available product brands."""
    return {"brands": sorted(BRANDS)}
