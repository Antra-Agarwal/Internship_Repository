"""
Abstract interface for retrievers.
"""

from abc import ABC, abstractmethod

from src.vectorstores.base import SearchResult


class BaseRetriever(ABC):
    """
    Abstract base class for retrievers.

    A retriever converts a text query into an embedding,
    searches the vector store, and returns the most
    relevant documents.
    """

    @abstractmethod
    def retrieve(
        self,
        query: str,
        k: int = 5,
    ) -> list[SearchResult]:
        """
        Retrieve the most relevant documents.

        Args:
            query: User query.
            k: Number of results.

        Returns:
            List of SearchResult objects.
        """
        raise NotImplementedError