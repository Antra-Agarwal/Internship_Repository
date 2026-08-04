"""
LangGraph node implementations.
"""

from src.llms import BaseLLM
from src.prompts.rag_prompt import RAG_PROMPT
from src.rerankers import BaseReranker
from src.retrievers import BaseRetriever

from .state import AgentState


class RetrievalNode:
    """
    Retrieves relevant documents and prepares context.
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        reranker: BaseReranker | None = None,
        retrieval_k: int = 10,
        final_k: int = 3,
    ):
        self._retriever = retriever
        self._reranker = reranker
        self._retrieval_k = retrieval_k
        self._final_k = final_k

    def __call__(
        self,
        state: AgentState,
    ) -> AgentState:

        results = self._retriever.retrieve(
            query=state["question"],
            k=self._retrieval_k,
        )

        if self._reranker is not None:
            results = self._reranker.rerank(
                query=state["question"],
                results=results,
                top_k=self._final_k,
            )
        else:
            results = results[: self._final_k]

        context = "\n\n".join(
            result.document.page_content
            for result in results
        )

        state["results"] = results
        state["context"] = context

        state["metadata"] = {
            "retrieved_documents": len(results),
            "retriever": type(self._retriever).__name__,
            "reranker": (
                type(self._reranker).__name__
                if self._reranker
                else None
            ),
        }

        return state


class GenerationNode:
    """
    Generates the final answer.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ):
        self._llm = llm

    def __call__(
            self,
            state: AgentState,
        ) -> AgentState:

        if state["context"]:
            prompt = RAG_PROMPT.format(
                context=state["context"],
                question=state["question"],
            )

        else:
            prompt = state["question"]

        state["answer"] = self._llm.generate(prompt)
        return state