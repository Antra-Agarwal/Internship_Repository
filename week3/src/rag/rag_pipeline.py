from src.llms import BaseLLM
from src.prompts.rag_prompt import RAG_PROMPT
from src.retrievers.base_retriever import BaseRetriever


class RAGPipeline:
    """
    End-to-end Retrieval-Augmented Generation pipeline.
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        llm: BaseLLM,
    ):
        self._retriever = retriever
        self._llm = llm

    def answer(
        self,
        question: str,
        k: int = 3,
    ) -> str:
        """
        Generate an answer using retrieved context.
        """

        results = self._retriever.retrieve(
            query=question,
            k=k,
        )

        context = "\n\n".join(
            result.document.page_content
            for result in results
        )

        prompt = RAG_PROMPT.format(
            context=context,
            question=question,
        )

        return self._llm.generate(prompt)