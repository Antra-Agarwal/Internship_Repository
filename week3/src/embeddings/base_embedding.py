from abc import ABC, abstractmethod


class BaseEmbedding(ABC):
    """
    Abstract base class for embedding models.

    Defines the interface that all embedding model
    implementations must follow.
    """

    @property
    @abstractmethod
    def embedding_client(self):
        """
        Return the underlying embedding client.

        This is primarily intended for integrations that require
        direct access to the underlying embedding implementation,
        such as LangChain's SemanticChunker.
        """
        raise NotImplementedError

    @abstractmethod
    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.

        Args:
            texts: List of input texts.

        Returns:
            List of embedding vectors.
        """
        raise NotImplementedError

    @abstractmethod
    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        """
        Generate an embedding for a single query.

        Args:
            query: Query text.

        Returns:
            Embedding vector.
        """
        raise NotImplementedError