from abc import ABC, abstractmethod
from dataclasses import dataclass

from .data_loader import DataLoader


@dataclass
class RecommendationResult:
    product_id: str
    score: float
    rank: int


class BaseRecommender(ABC):
    """
    Abstract base class for Content-Based Recommenders.
    Every recommender must implement fit() and recommend().
    """

    def __init__(self, data_loader: DataLoader):
        """
        Initialise recommender with a shared DataLoader instance.
        """
        self.data_loader = data_loader

    @abstractmethod
    def fit(self) -> None:
        """
        Train/fit the model (e.g., build TF-IDF matrices, train Word2Vec).
        Raises an error if data_loader.is_loaded is False.
        """
        pass

    @abstractmethod
    def recommend(self, user_id: str, k: int = 5) -> list[RecommendationResult]:
        """
        Return top k recommended products for a given user.
        Raises KeyError if user_id is not found.
        """
        pass
