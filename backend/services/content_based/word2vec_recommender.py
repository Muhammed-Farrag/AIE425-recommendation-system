import logging
import numpy as np
from gensim.models import Word2Vec
from sklearn.metrics.pairwise import cosine_similarity

from .base_recommender import BaseRecommender, RecommendationResult

logger = logging.getLogger(__name__)

W2V_VECTOR_SIZE = 100
W2V_WINDOW = 5
W2V_MIN_COUNT = 1

class Word2VecRecommender(BaseRecommender):
    def __init__(self, data_loader):
        super().__init__(data_loader)
        self.model = None
        self._w2v_matrix = None

    def fit(self) -> None:
        if not self.data_loader.is_loaded:
            raise RuntimeError("DataLoader must be loaded before fitting.")
        
        texts = self.data_loader.get_texts_in_order()
        # Tokenize texts for gensim Word2Vec
        tokenized_texts = [text.split() for text in texts]
        
        self.model = Word2Vec(
            sentences=tokenized_texts,
            vector_size=W2V_VECTOR_SIZE,
            window=W2V_WINDOW,
            min_count=W2V_MIN_COUNT,
            workers=4,
            seed=42
        )
        
        # Build document vectors by averaging word vectors
        doc_vectors = []
        for tokens in tokenized_texts:
            vecs = [self.model.wv[word] for word in tokens if word in self.model.wv]
            if vecs:
                doc_vectors.append(np.mean(vecs, axis=0))
            else:
                doc_vectors.append(np.zeros(W2V_VECTOR_SIZE))
                
        self._w2v_matrix = np.vstack(doc_vectors)
        logger.info(f"Word2VecRecommender fitted. Matrix shape: {self._w2v_matrix.shape}")

    def recommend(self, user_id: str, k: int = 5) -> list[RecommendationResult]:
        if self._w2v_matrix is None:
            raise RuntimeError("Model must be fitted before recommend() is called.")
            
        pos_pids = self.data_loader.get_user_positive_products(user_id)
        if not pos_pids:
            return []

        all_pids = self.data_loader.all_product_ids
        pid_to_idx = {pid: idx for idx, pid in enumerate(all_pids)}
        pos_indices = [pid_to_idx[pid] for pid in pos_pids if pid in pid_to_idx]
        
        if not pos_indices:
            return []

        # Compute user profile in Word2Vec space
        user_profile = self._w2v_matrix[pos_indices].mean(axis=0).reshape(1, -1)
        
        # Calculate similarities against all items
        similarities = cosine_similarity(user_profile, self._w2v_matrix).flatten()
        
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
