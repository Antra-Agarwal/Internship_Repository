"""
Retriever implementation using a vector store.
"""

from src.embeddings.base_embedding import BaseEmbedding
from src.retrievers.base_retriever import BaseRetriever
from src.vectorstores.base import (
    BaseVectorStore,
    SearchResult,
)


class VectorStoreRetriever(BaseRetriever):
    """
    Retriever backed by a vector store.

    The retriever converts a user query into an embedding,
    searches the vector store, and optionally filters
    results based on a maximum distance threshold.
    """

    def __init__(
        self,
        embedding_model: BaseEmbedding,
        vector_store: BaseVectorStore,
    ):
        """
        Initialize the retriever.

        Args:
            embedding_model: Embedding model used to embed queries.
            vector_store: Vector store used for similarity search.
        """
        self.embedding_model = embedding_model
        self.vector_store = vector_store

    def retrieve(
        self,
        query: str,
        k: int = 5,
        max_distance: float | None = None,
    ) -> list[SearchResult]:
        """
        Retrieve the top-k most relevant documents.

        Args:
            query: User query.
            k: Number of documents to retrieve.
            max_distance: Maximum allowed L2 distance.
                Results having a larger distance are discarded.
                If None, no threshold is applied.

        Returns:
            List of SearchResult objects.
        """

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        if k <= 0:
            raise ValueError(
                "k must be greater than zero."
            )

        if (
            max_distance is not None
            and max_distance < 0
        ):
            raise ValueError(
                "max_distance must be non-negative."
            )

        query_embedding = self.embedding_model.embed_query(
            query
        )

        results = self.vector_store.search(
            query_embedding=query_embedding,
            k=k,
        )

        if max_distance is None:
            return results

        return [
            result
            for result in results
            if result.score <= max_distance
        ]