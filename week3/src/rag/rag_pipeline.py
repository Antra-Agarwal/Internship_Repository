"""
End-to-end Retrieval-Augmented Generation pipeline.
"""

from src.llms import BaseLLM
from src.prompts.rag_prompt import RAG_PROMPT
from src.rerankers import BaseReranker
from src.retrievers.base_retriever import BaseRetriever


class RAGPipeline:
    """
    End-to-end Retrieval-Augmented Generation pipeline.
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        llm: BaseLLM,
        reranker: BaseReranker | None = None,
    ):
        """
        Initialize the RAG pipeline.

        Args:
            retriever: Document retriever.
            llm: Language model.
            reranker: Optional reranker.
        """

        self._retriever = retriever
        self._llm = llm
        self._reranker = reranker

    def answer(
        self,
        question: str,
        k: int = 3,
        retrieval_k: int = 10,
    ) -> str:
        """
        Generate an answer using retrieved context.

        Args:
            question: User question.
            k: Number of documents after reranking.
            retrieval_k: Number of documents initially retrieved.

        Returns:
            Generated answer.
        """

        results = self._retriever.retrieve(
            query=question,
            k=retrieval_k,
        )

        if self._reranker is not None:

            results = self._reranker.rerank(
                query=question,
                results=results,
                top_k=k,
            )

        else:
            results = results[:k]

        context = "\n\n".join(
            result.document.page_content
            for result in results
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        return self._llm.generate(prompt)