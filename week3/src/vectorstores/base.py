"""
Abstract interface for vector stores.

Every vector database implementation (FAISS, ChromaDB, Pinecone, etc.)
should inherit from this class.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

from langchain_core.documents import Document


@dataclass(slots=True)
class SearchResult:
    """
    Represents a single similarity search result.
    """

    document: Document
    score: float


class BaseVectorStore(ABC):
    """
    Abstract base class for vector stores.
    """

    @abstractmethod
    def add(
        self,
        embeddings: list[list[float]],
        documents: list[Document],
    ) -> None:
        """
        Add embeddings and their corresponding documents.

        Args:
            embeddings: Embedding vectors.
            documents: Corresponding LangChain documents.
        """
        raise NotImplementedError

    @abstractmethod
    def search(
        self,
        query_embedding: list[float],
        k: int = 5,
    ) -> list[SearchResult]:
        """
        Search for the top-k most similar documents.

        Args:
            query_embedding: Query embedding.
            k: Number of nearest neighbours.

        Returns:
            List of SearchResult objects.
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, path: str) -> None:
        """
        Save the vector store.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, path: str) -> None:
        """
        Load the vector store.
        """
        raise NotImplementedError

    @abstractmethod
    def __len__(self) -> int:
        """
        Number of indexed vectors.
        """
        raise NotImplementedError