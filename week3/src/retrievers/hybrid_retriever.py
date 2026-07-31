"""
Hybrid Retriever using Reciprocal Rank Fusion (RRF).
"""

from src.retrievers.base_retriever import BaseRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.vectorstore_retriever import VectorStoreRetriever
from src.vectorstores.base import SearchResult


class HybridRetriever(BaseRetriever):
    """
    Hybrid retriever combining dense retrieval and BM25
    using Reciprocal Rank Fusion (RRF).
    """

    def __init__(
        self,
        vector_retriever: VectorStoreRetriever,
        bm25_retriever: BM25Retriever,
    ):
        self.vector_retriever = vector_retriever
        self.bm25_retriever = bm25_retriever

    @staticmethod
    def _doc_key(result: SearchResult):
        """
        Create a stable key for each document chunk.
        """

        return (
            result.document.metadata.get("source"),
            result.document.metadata.get("page"),
            result.document.page_content,
        )

    def retrieve(
        self,
        query: str,
        k: int = 5,
        metadata_filter: dict | None = None,
        rrf_k: int = 60,
        **kwargs,
    ) -> list[SearchResult]:
        """
        Retrieve documents using Reciprocal Rank Fusion.

        Args:
            query: User query.
            k: Number of final documents to return.
            metadata_filter: Optional metadata filter.
            rrf_k: RRF constant (default = 60).

        Returns:
            Ranked SearchResult objects.
        """

        candidate_k = max(20, k * 4)

        dense_results = self.vector_retriever.retrieve(
            query=query,
            k=candidate_k,
            metadata_filter=metadata_filter,
        )

        sparse_results = self.bm25_retriever.retrieve(
            query=query,
            k=candidate_k,
            metadata_filter=metadata_filter,
        )

        fused: dict = {}

        for rank, result in enumerate(dense_results, start=1):

            key = self._doc_key(result)

            if key not in fused:
                fused[key] = {
                    "document": result.document,
                    "score": 0.0,
                }

            fused[key]["score"] += 1 / (rrf_k + rank)

        for rank, result in enumerate(sparse_results, start=1):

            key = self._doc_key(result)

            if key not in fused:
                fused[key] = {
                    "document": result.document,
                    "score": 0.0,
                }

            fused[key]["score"] += 1 / (rrf_k + rank)

        results = [
            SearchResult(
                document=value["document"],
                score=value["score"],
            )
            for value in fused.values()
        ]

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:k]