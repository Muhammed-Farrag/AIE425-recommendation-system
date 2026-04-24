"""
Data Manager - Handles all data operations
"""

import json
from typing import List, Dict, Optional

class DataManager:
    """Manages all data for the recommender system"""
    
    def __init__(self):
        """Initialize data manager with mock data"""
        self.users = self._init_users()
        self.products = self._init_products()
        self.ratings = self._init_ratings()
    
    def _init_users(self) -> List[Dict]:
        """Initialize mock users"""
        return [
            {
                "id": 1,
                "name": "Ahmed Hassan",
                "preferences": ["Electronics", "Premium"],
                "budget": 500
            },
            {
                "id": 2,
                "name": "Fatima Ali",
                "preferences": ["Accessories", "Budget-friendly"],
                "budget": 100
            },
            {
                "id": 3,
                "name": "Mohammed Karim",
                "preferences": ["Electronics", "Audio"],
                "budget": 300
            },
            {
                "id": 4,
                "name": "Noor Ibrahim",
                "preferences": ["Accessories", "Premium"],
                "budget": 200
            },
            {
                "id": 5,
                "name": "Sara Mahmoud",
                "preferences": ["Electronics", "Accessories"],
                "budget": 400
            }
        ]
    
    def _init_products(self) -> List[Dict]:
        """Initialize mock products"""
        return [
            {
                "id": 1,
                "name": "Wireless Headphones Pro",
                "category": "Electronics",
                "price": 199.99,
                "brand": "AudioMax",
                "rating": 4.5,
                "description": "Premium wireless headphones with noise cancellation",
                "tags": ["audio", "wireless", "premium", "noise-cancelling"]
            },
            {
                "id": 2,
                "name": "Smart Watch Ultra",
                "category": "Electronics",
                "price": 299.99,
                "brand": "TechTime",
                "rating": 4.3,
                "description": "Advanced smartwatch with health monitoring",
                "tags": ["wearable", "health", "smart", "fitness"]
            },
            {
                "id": 3,
                "name": "Portable Phone Charger",
                "category": "Accessories",
                "price": 49.99,
                "brand": "PowerBank",
                "rating": 4.7,
                "description": "Fast charging portable power bank",
                "tags": ["charging", "portable", "fast-charge", "accessories"]
            },
            {
                "id": 4,
                "name": "USB-C Cable 3m",
                "category": "Accessories",
                "price": 19.99,
                "brand": "CableMax",
                "rating": 4.4,
                "description": "High-speed USB-C charging cable",
                "tags": ["cable", "charging", "usb-c", "accessories"]
            },
            {
                "id": 5,
                "name": "Bluetooth Speaker",
                "category": "Electronics",
                "price": 79.99,
                "brand": "SoundWave",
                "rating": 4.6,
                "description": "Portable waterproof Bluetooth speaker",
                "tags": ["audio", "wireless", "waterproof", "portable"]
            },
            {
                "id": 6,
                "name": "Phone Screen Protector",
                "category": "Accessories",
                "price": 9.99,
                "brand": "ScreenGuard",
                "rating": 4.5,
                "description": "Tempered glass screen protector",
                "tags": ["protection", "glass", "accessories", "durable"]
            },
            {
                "id": 7,
                "name": "Laptop Stand",
                "category": "Accessories",
                "price": 39.99,
                "brand": "DeskPro",
                "rating": 4.2,
                "description": "Adjustable aluminum laptop stand",
                "tags": ["ergonomic", "desk", "accessories", "adjustable"]
            },
            {
                "id": 8,
                "name": "Wireless Mouse",
                "category": "Electronics",
                "price": 59.99,
                "brand": "TechMouse",
                "rating": 4.4,
                "description": "Precision wireless mouse with long battery life",
                "tags": ["wireless", "mouse", "computer", "precision"]
            },
            {
                "id": 9,
                "name": "USB Hub 4-Port",
                "category": "Accessories",
                "price": 29.99,
                "brand": "HubTech",
                "rating": 4.3,
                "description": "Multi-port USB hub for connectivity",
                "tags": ["hub", "connectivity", "accessories", "usb"]
            },
            {
                "id": 10,
                "name": "Phone Case Premium",
                "category": "Accessories",
                "price": 24.99,
                "brand": "CaseShield",
                "rating": 4.6,
                "description": "Durable protective phone case",
                "tags": ["protection", "case", "accessories", "durable"]
            }
        ]
    
    def _init_ratings(self) -> List[Dict]:
        """Initialize mock user ratings"""
        return [
            {"userId": 1, "productId": 1, "rating": 5},
            {"userId": 1, "productId": 3, "rating": 4},
            {"userId": 1, "productId": 5, "rating": 5},
            {"userId": 1, "productId": 7, "rating": 3},
            
            {"userId": 2, "productId": 2, "rating": 4},
            {"userId": 2, "productId": 4, "rating": 5},
            {"userId": 2, "productId": 6, "rating": 4},
            {"userId": 2, "productId": 8, "rating": 5},
            
            {"userId": 3, "productId": 1, "rating": 4},
            {"userId": 3, "productId": 2, "rating": 3},
            {"userId": 3, "productId": 5, "rating": 5},
            {"userId": 3, "productId": 9, "rating": 4},
            
            {"userId": 4, "productId": 3, "rating": 5},
            {"userId": 4, "productId": 4, "rating": 4},
            {"userId": 4, "productId": 7, "rating": 5},
            {"userId": 4, "productId": 10, "rating": 3},
            
            {"userId": 5, "productId": 2, "rating": 5},
            {"userId": 5, "productId": 6, "rating": 5},
            {"userId": 5, "productId": 8, "rating": 4},
            {"userId": 5, "productId": 9, "rating": 5},
        ]
    
    # ============ User Methods ============
    
    def get_all_users(self) -> List[Dict]:
        """Get all users"""
        return self.users
    
    def get_user(self, user_id: int) -> Optional[Dict]:
        """Get user by ID"""
        for user in self.users:
            if user["id"] == user_id:
                return user
        return None
    
    def get_user_ratings(self, user_id: int) -> List[Dict]:
        """Get all ratings for a user"""
        return [r for r in self.ratings if r["userId"] == user_id]
    
    # ============ Product Methods ============
    
    def get_all_products(self) -> List[Dict]:
        """Get all products"""
        return self.products
    
    def get_product(self, product_id: int) -> Optional[Dict]:
        """Get product by ID"""
        for product in self.products:
            if product["id"] == product_id:
                return product
        return None
    
    def get_products_by_category(self, category: str) -> List[Dict]:
        """Get products by category"""
        return [p for p in self.products if p["category"].lower() == category.lower()]
    
    def get_products_by_price_range(self, min_price: float, max_price: float) -> List[Dict]:
        """Get products within price range"""
        return [p for p in self.products if min_price <= p["price"] <= max_price]
    
    # ============ Rating Methods ============
    
    def get_all_ratings(self) -> List[Dict]:
        """Get all ratings"""
        return self.ratings
    
    def get_product_ratings(self, product_id: int) -> List[Dict]:
        """Get all ratings for a product"""
        return [r for r in self.ratings if r["productId"] == product_id]
    
    def get_average_rating(self, product_id: int) -> float:
        """Get average rating for a product"""
        ratings = self.get_product_ratings(product_id)
        if not ratings:
            return 0.0
        return sum(r["rating"] for r in ratings) / len(ratings)
    
    # ============ Similarity Methods ============
    
    def calculate_user_similarity(self, user_id1: int, user_id2: int) -> float:
        """Calculate similarity between two users based on ratings"""
        ratings1 = {r["productId"]: r["rating"] for r in self.get_user_ratings(user_id1)}
        ratings2 = {r["productId"]: r["rating"] for r in self.get_user_ratings(user_id2)}
        
        # Find common products
        common_products = set(ratings1.keys()) & set(ratings2.keys())
        
        if not common_products:
            return 0.0
        
        # Calculate Pearson correlation
        sum_xy = sum((ratings1[p] - 3) * (ratings2[p] - 3) for p in common_products)
        sum_x2 = sum((ratings1[p] - 3) ** 2 for p in common_products)
        sum_y2 = sum((ratings2[p] - 3) ** 2 for p in common_products)
        
        denominator = (sum_x2 * sum_y2) ** 0.5
        
        if denominator == 0:
            return 0.0
        
        return sum_xy / denominator
    
    def calculate_product_similarity(self, product_id1: int, product_id2: int) -> float:
        """Calculate similarity between two products based on tags"""
        product1 = self.get_product(product_id1)
        product2 = self.get_product(product_id2)
        
        if not product1 or not product2:
            return 0.0
        
        tags1 = set(product1["tags"])
        tags2 = set(product2["tags"])
        
        if not tags1 or not tags2:
            return 0.0
        
        # Jaccard similarity
        intersection = len(tags1 & tags2)
        union = len(tags1 | tags2)
        
        return intersection / union if union > 0 else 0.0
    
    # ============ User Management Methods ============
    
    def add_user(self, name: str, preferences: List[str], budget: float) -> Dict:
        """Add a new user to the system"""
        # Generate new user ID
        new_id = max([u["id"] for u in self.users]) + 1 if self.users else 1
        
        # Create new user
        new_user = {
            "id": new_id,
            "name": name,
            "preferences": preferences,
            "budget": budget
        }
        
        # Add to users list
        self.users.append(new_user)
        
        return new_user
    
    def get_next_user_id(self) -> int:
        """Get the next available user ID"""
        return max([u["id"] for u in self.users]) + 1 if self.users else 1
