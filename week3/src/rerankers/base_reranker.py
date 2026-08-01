"""
Abstract interface for rerankers.
"""

from abc import ABC, abstractmethod

from src.vectorstores.base import SearchResult


class BaseReranker(ABC):
    """
    Abstract base class for rerankers.
    """

    @abstractmethod
    def rerank(
        self,
        query: str,
        results: list[SearchResult],
        top_k: int,
    ) -> list[SearchResult]:
        """
        Re-rank retrieved documents.

        Args:
            query: User query.
            results: Retrieved documents.
            top_k: Number of final documents.

        Returns:
            Re-ranked search results.
        """
        raise NotImplementedError