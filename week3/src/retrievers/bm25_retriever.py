"""
BM25 retriever implementation.
"""

import re

from rank_bm25 import BM25Okapi

from src.retrievers.base_retriever import BaseRetriever
from src.vectorstores.base import SearchResult
from src.vectorstores.faiss_store import FAISSVectorStore


class BM25Retriever(BaseRetriever):
    """
    Sparse retriever using the BM25 ranking algorithm.
    """

    STOPWORDS = {
        "a",
        "an",
        "and",
        "are",
        "as",
        "at",
        "be",
        "by",
        "for",
        "from",
        "has",
        "have",
        "in",
        "is",
        "it",
        "of",
        "on",
        "or",
        "that",
        "the",
        "their",
        "this",
        "to",
        "was",
        "were",
        "what",
        "when",
        "where",
        "which",
        "who",
        "why",
        "with",
    }

    def __init__(
        self,
        vector_store: FAISSVectorStore,
    ):
        """
        Initialize the BM25 retriever.

        Args:
            vector_store: FAISS vector store containing indexed documents.
        """

        self.vector_store = vector_store
        self.documents = vector_store.documents

        self.corpus = [
            self._tokenize(document.page_content)
            for document in self.documents
        ]

        self.bm25 = BM25Okapi(self.corpus)

    @classmethod
    def _tokenize(
        cls,
        text: str,
    ) -> list[str]:
        """
        Normalize and tokenize text.

        Steps:
        1. Convert to lowercase.
        2. Remove punctuation.
        3. Split into tokens.
        4. Remove stopwords.
        """

        text = text.lower()

        text = re.sub(
            r"[^a-z0-9\s]",
            " ",
            text,
        )

        tokens = text.split()

        tokens = [
            token
            for token in tokens
            if token not in cls.STOPWORDS
        ]

        return tokens

    def retrieve(
        self,
        query: str,
        k: int = 5,
        metadata_filter: dict | None = None,
        **kwargs,
    ) -> list[SearchResult]:
        """
        Retrieve relevant documents using BM25.

        Args:
            query: User query.
            k: Number of documents.
            metadata_filter: Optional metadata filter.

        Returns:
            List of SearchResult objects.
        """

        if not query.strip():
            raise ValueError(
                "Query cannot be empty."
            )

        if k <= 0:
            raise ValueError(
                "k must be greater than zero."
            )

        query_tokens = self._tokenize(query)

        scores = self.bm25.get_scores(
            query_tokens
        )

        results: list[SearchResult] = []

        for score, document in zip(
            scores,
            self.documents,
        ):

            if metadata_filter is not None:

                if not all(
                    document.metadata.get(key) == value
                    for key, value in metadata_filter.items()
                ):
                    continue

            results.append(
                SearchResult(
                    document=document,
                    score=float(score),
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:k]