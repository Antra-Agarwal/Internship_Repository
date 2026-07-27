from abc import ABC, abstractmethod

import numpy as np


class SimilarityStrategy(ABC):
    """
    Base class for semantic similarity strategies.
    """

    @abstractmethod
    def compute_similarities(
        self,
        embeddings: list[list[float]]
    ) -> list[float]:
        """
        Compute similarity scores from embeddings.

        Args:
            embeddings: List of embedding vectors.

        Returns:
            List of similarity scores.
        """
        pass


class AdjacentSimilarityStrategy(SimilarityStrategy):
    """
    Computes cosine similarity between adjacent embedding vectors.
    """

    @staticmethod
    def cosine_similarity(
        vector1: list[float],
        vector2: list[float]
    ) -> float:
        """
        Compute cosine similarity between two embedding vectors.
        """

        v1 = np.asarray(vector1)
        v2 = np.asarray(vector2)

        denominator = np.linalg.norm(v1) * np.linalg.norm(v2)

        if denominator == 0:
            return 0.0

        return float(np.dot(v1, v2) / denominator)

    def compute_similarities(
        self,
        embeddings: list[list[float]]
    ) -> list[float]:
        """
        Compute cosine similarity between adjacent embeddings.

        Example:
            E1 <-> E2
            E2 <-> E3
            E3 <-> E4
        """

        if len(embeddings) < 2:
            return []

        similarities = []

        for i in range(len(embeddings) - 1):
            similarities.append(
                self.cosine_similarity(
                    embeddings[i],
                    embeddings[i + 1]
                )
            )

        return similarities