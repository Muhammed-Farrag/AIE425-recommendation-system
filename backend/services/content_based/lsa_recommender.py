import logging
import numpy as np
from sklearn.decomposition import TruncatedSVD
from sklearn.metrics.pairwise import cosine_similarity

from .base_recommender import BaseRecommender, RecommendationResult
from .tfidf_recommender import TFIDFRecommender

logger = logging.getLogger(__name__)

LSA_N_COMPONENTS = 100

class LSARecommender(BaseRecommender):
    def __init__(self, data_loader, tfidf_recommender: TFIDFRecommender):
        super().__init__(data_loader)
        self._tfidf_recommender = tfidf_recommender
        self.svd = None
        self._lsa_matrix = None

    def fit(self) -> None:
        if not self.data_loader.is_loaded:
            raise RuntimeError("DataLoader must be loaded before fitting.")
        if self._tfidf_recommender._tfidf_matrix is None:
            raise RuntimeError("TFIDFRecommender must be fitted before LSARecommender.")
            
        tfidf_matrix = self._tfidf_recommender._tfidf_matrix
        safe_components = min(LSA_N_COMPONENTS, tfidf_matrix.shape[0] - 1)
        safe_components = max(2, safe_components) # Ensure at least 2 components
        
        self.svd = TruncatedSVD(n_components=safe_components, random_state=42)
        self._lsa_matrix = self.svd.fit_transform(tfidf_matrix)
        
        logger.info(f"LSARecommender fitted. Matrix shape: {self._lsa_matrix.shape}")

    def recommend(self, user_id: str, k: int = 5) -> list[RecommendationResult]:
        if self._lsa_matrix is None:
            raise RuntimeError("Model must be fitted before recommend() is called.")
            
        pos_pids = self.data_loader.get_user_positive_products(user_id)
        if not pos_pids:
            return []

        all_pids = self.data_loader.all_product_ids
        pid_to_idx = {pid: idx for idx, pid in enumerate(all_pids)}
        pos_indices = [pid_to_idx[pid] for pid in pos_pids if pid in pid_to_idx]
        
        if not pos_indices:
            return []

        # Compute user profile in LSA space
        user_profile = self._lsa_matrix[pos_indices].mean(axis=0).reshape(1, -1)
        
        # Calculate similarities against all items
        similarities = cosine_similarity(user_profile, self._lsa_matrix).flatten()
        
        # Exclude interacted items
        interacted_pids = self.data_loader.user_products.get(user_id, set())
        for pid in interacted_pids:
            if pid in pid_to_idx:
                similarities[pid_to_idx[pid]] = -1.0
                
        # Get top k indices
        top_indices = np.argsort(similarities)[::-1][:k]
        
        results = []
        for rank, idx in enumerate(top_indices, start=1):
            if similarities[idx] > -1.0:
                results.append(
                    RecommendationResult(
                        product_id=all_pids[idx],
                        score=float(similarities[idx]),
                        rank=rank
                    )
                )
        return results
