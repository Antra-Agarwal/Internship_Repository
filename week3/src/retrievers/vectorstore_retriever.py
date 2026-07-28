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
    searches the vector store, and returns the most relevant
    documents.
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
    ) -> list[SearchResult]:
        """
        Retrieve the top-k most relevant documents.

        Args:
            query: User query.
            k: Number of documents to retrieve.

        Returns:
            List of SearchResult objects.
        """

        if not query.strip():
            raise ValueError("Query cannot be empty.")

        query_embedding = self.embedding_model.embed_query(query)

        return self.vector_store.search(
            query_embedding=query_embedding,
            k=k,
        )