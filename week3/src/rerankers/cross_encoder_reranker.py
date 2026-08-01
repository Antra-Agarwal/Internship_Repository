"""
Cross-Encoder reranker implementation.
"""

from sentence_transformers import CrossEncoder

from src.rerankers.base_reranker import BaseReranker
from src.vectorstores.base import SearchResult


class CrossEncoderReranker(BaseReranker):
    """
    Cross-Encoder based reranker.
    """

    def __init__(
        self,
        model_name: str = (
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        ),
    ):
        """
        Initialize the reranker.

        Args:
            model_name: Hugging Face model.
        """

        self.model = CrossEncoder(model_name)

    def rerank(
        self,
        query: str,
        results: list[SearchResult],
        top_k: int,
    ) -> list[SearchResult]:
        """
        Re-rank retrieved documents.
        """

        if not results:
            return []

        pairs = [
            (
                query,
                result.document.page_content,
            )
            for result in results
        ]

        scores = self.model.predict(pairs)

        reranked = []

        for result, score in zip(
            results,
            scores,
        ):

            reranked.append(
                SearchResult(
                    document=result.document,
                    score=float(score),
                )
            )

        reranked.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return reranked[:top_k]