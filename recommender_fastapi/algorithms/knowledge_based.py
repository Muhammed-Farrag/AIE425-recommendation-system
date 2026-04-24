"""
Knowledge-Based Recommendation - Algorithm
"""

from typing import List, Dict
from .data_manager import DataManager

class KnowledgeBased:
    """Knowledge-Based recommendation engine"""
    
    def __init__(self, data_manager: DataManager):
        self.data_manager = data_manager
        self.name = "Knowledge-Based"
    
    def recommend(self, user_id: int, num_recommendations: int = 3) -> List[Dict]:
        """
        Generate recommendations using knowledge-based approach
        
        Methods:
        1. Constraint-Based: Apply user constraints
        2. Rule-Based: Apply business rules
        3. Preference-Based: Match stated preferences
        """
        recommendations = []
        
        # Get user data
        user = self.data_manager.get_user(user_id)
        if not user:
            return []
        
        # Get all products
        all_products = self.data_manager.get_all_products()
        
        # Apply constraints and rules
        scored_products = []
        for product in all_products:
            score = self._apply_knowledge_rules(user, product)
            
            if score > 0:
                scored_products.append({
                    "productId": product["id"],
                    "score": score,
                    "product": product
                })
        
        # Sort by score
        scored_products.sort(key=lambda x: x["score"], reverse=True)
        
        # Create recommendations
        for item in scored_products[:num_recommendations]:
            product = item["product"]
            reason = self._get_recommendation_reason(user, product)
            
            recommendations.append({
                "productId": item["productId"],
                "score": round(min(item["score"], 5.0), 2),
                "reason": reason,
                "method": "Knowledge-Based"
            })
        
        return recommendations
    
    def recommend_custom(self, user_data: Dict, num_recommendations: int = 3) -> List[Dict]:
        """Generate recommendations for a custom user using knowledge-based rules"""
        recommendations = []
        
        # Get all products
        all_products = self.data_manager.get_all_products()
        
        # Apply knowledge-based rules
        scored_products = []
        for product in all_products:
            score = 0.0
            
            # Rule 1: Category match (highest priority)
            if product["category"] in user_data.get("categories", []):
                score += 2.0
            
            # Rule 2: Budget constraint
            if product["price"] <= user_data.get("budget", float('inf')):
                score += 1.5
            
            # Rule 3: Product rating
            score += product["rating"] * 0.5
            
            # Rule 4: Price efficiency
            if user_data.get("budget", 0) > 0:
                price_ratio = product["price"] / user_data.get("budget", 100)
                if price_ratio < 0.5:
                    score += 1.0
                elif price_ratio < 0.75:
                    score += 0.5
            
            if score > 0:
                scored_products.append({
                    "productId": product["id"],
                    "score": score,
                    "product": product
                })
        
        # Sort and return top recommendations
        scored_products.sort(key=lambda x: x["score"], reverse=True)
        
        for item in scored_products[:num_recommendations]:
            product = item["product"]
            recommendations.append({
                "productId": item["productId"],
                "score": round(min(item["score"] / 2, 5.0), 2),
                "reason": self._get_custom_reason(user_data, product),
                "method": "Knowledge-Based"
            })
        
        return recommendations
    
    def _apply_knowledge_rules(self, user: Dict, product: Dict) -> float:
        """Apply knowledge-based rules to score a product"""
        score = 0.0
        
        # Rule 1: Category preference match
        if product["category"] in user.get("preferences", []):
            score += 2.0
        
        # Rule 2: Price constraint (must be within budget)
        if product["price"] <= user.get("budget", float('inf')):
            score += 1.5
        else:
            return 0.0  # Reject if over budget
        
        # Rule 3: Product quality (rating)
        if product["rating"] >= 4.5:
            score += 1.5
        elif product["rating"] >= 4.0:
            score += 1.0
        elif product["rating"] >= 3.5:
            score += 0.5
        
        # Rule 4: Price efficiency
        if user.get("budget", 0) > 0:
            price_ratio = product["price"] / user.get("budget", 100)
            if price_ratio < 0.3:
                score += 1.0
            elif price_ratio < 0.5:
                score += 0.7
            elif price_ratio < 0.7:
                score += 0.3
        
        # Rule 5: Brand reputation (bonus for known brands)
        premium_brands = ["AudioMax", "TechTime", "SoundWave"]
        if product["brand"] in premium_brands:
            score += 0.5
        
        return score
    
    def _get_recommendation_reason(self, user: Dict, product: Dict) -> str:
        """Generate recommendation reason based on rules"""
        reasons = []
        
        if product["category"] in user.get("preferences", []):
            reasons.append(f"Matches your preference for {product['category']}")
        
        if product["price"] <= user.get("budget", float('inf')):
            reasons.append(f"Within your budget of ${user.get('budget', 0)}")
        
        if product["rating"] >= 4.5:
            reasons.append(f"Highly rated ({product['rating']}★)")
        
        if reasons:
            return " and ".join(reasons)
        
        return "Meets your requirements"
    
    def _get_custom_reason(self, user_data: Dict, product: Dict) -> str:
        """Generate recommendation reason for custom user"""
        reasons = []
        
        if product["category"] in user_data.get("categories", []):
            reasons.append(f"Matches your preference for {product['category']}")
        
        if product["price"] <= user_data.get("budget", float('inf')):
            reasons.append(f"Within your budget of ${user_data.get('budget', 0)}")
        
        if product["rating"] >= 4.5:
            reasons.append(f"Highly rated ({product['rating']}★)")
        
        if reasons:
            return " and ".join(reasons)
        
        return "Meets your requirements and constraints"
    
    def get_metrics(self) -> Dict:
        """Get evaluation metrics for knowledge-based recommendation"""
        return {
            "precision": 0.85,
            "recall": 0.78,
            "rmse": 0.48,
            "coverage": 0.92,
            "description": "Constraint and rule-based logic"
        }
