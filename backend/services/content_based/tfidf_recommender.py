import logging
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from .base_recommender import BaseRecommender, RecommendationResult

logger = logging.getLogger(__name__)

TFIDF_MAX_FEATURES = 5000
TFIDF_MIN_DF = 1


class TFIDFRecommender(BaseRecommender):
    def __init__(self, data_loader):
        super().__init__(data_loader)
        self.vectorizer = TfidfVectorizer(
            max_features=TFIDF_MAX_FEATURES,
            min_df=TFIDF_MIN_DF,
            stop_words='english'
        )
        self._tfidf_matrix = None

    def fit(self) -> None:
        if not self.data_loader.is_loaded:
            raise RuntimeError("DataLoader must be loaded before fitting.")
        
        texts = self.data_loader.get_texts_in_order()
        self._tfidf_matrix = self.vectorizer.fit_transform(texts)
        logger.info(f"TFIDFRecommender fitted. Matrix shape: {self._tfidf_matrix.shape}")

    def recommend(self, user_id: str, k: int = 5) -> list[RecommendationResult]:
        if self._tfidf_matrix is None:
            raise RuntimeError("Model must be fitted before recommend() is called.")
        
        # Get positive products
        pos_pids = self.data_loader.get_user_positive_products(user_id)
        if not pos_pids:
            return []

        # Find indices of user's positive products
        all_pids = self.data_loader.all_product_ids
        pid_to_idx = {pid: idx for idx, pid in enumerate(all_pids)}
        pos_indices = [pid_to_idx[pid] for pid in pos_pids if pid in pid_to_idx]
        
        if not pos_indices:
            return []

        # Compute user profile by averaging TF-IDF vectors of positive items
        user_profile = self._tfidf_matrix[pos_indices].mean(axis=0)
        
        # Calculate similarities against all items
        # user_profile is 1 x V, _tfidf_matrix is N x V
        similarities = cosine_similarity(np.asarray(user_profile), self._tfidf_matrix).flatten()
        
        # Exclude already interacted items (so we don't recommend what they already bought)
        # However, Phase 2 spec: often we exclude, let's exclude all items they interacted with
        # from data_loader.user_products[user_id]
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
