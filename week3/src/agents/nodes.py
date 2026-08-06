"""
LangGraph node implementations.
"""

from src.llms import BaseLLM
from src.prompts.rag_prompt import RAG_PROMPT
from src.rerankers import BaseReranker
from src.retrievers import BaseRetriever
from src.utils.logger import get_logger

from .state import AgentState


class RetrievalNode:
    """
    LangGraph node responsible for document retrieval.

    Responsibilities:
    1. Retrieve relevant documents.
    2. Apply reranking (optional).
    3. Validate retrieval quality.
    4. Build the context string.
    5. Store retrieval information in the graph state.
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        reranker: BaseReranker | None = None,
        retrieval_k: int = 10,
        final_k: int = 3,
        rerank_threshold: float = 0.0,
    ):
        self._retriever = retriever
        self._reranker = reranker
        self._retrieval_k = retrieval_k
        self._final_k = final_k
        self._rerank_threshold = rerank_threshold
        self._logger = get_logger(
            self.__class__.__name__
        )

    def __call__(
        self,
        state: AgentState,
    ) -> AgentState:
        """
        Execute the retrieval step.
        """

        results = self._retriever.retrieve(
            query=state["question"],
            k=self._retrieval_k,
        )

        self._logger.info(
            f"Retrieved {len(results)} documents."
        )

        if self._reranker is not None:

            results = self._reranker.rerank(
                query=state["question"],
                results=results,
                top_k=self._final_k,
            )
            self._logger.info(
                f"Reranked to {len(results)} documents."
            )   

            # Validate reranked results
            if (
                not results
                or results[0].score < self._rerank_threshold
            ):
                results = []

        else:

            results = results[: self._final_k]

        if results:

            context = "\n\n".join(
                result.document.page_content
                for result in results
            )

        else:

            context = ""

        state["results"] = results
        state["context"] = context

        state["metadata"].update(
            {
                "route": "retrieve",
                "retrieval_success": len(results) > 0,
                "retrieved_documents": len(results),
                "retriever": type(self._retriever).__name__,
                "reranker": (
                    type(self._reranker).__name__
                    if self._reranker is not None
                    else None
                ),
            }
        )

        return state


class GenerationNode:
    """
    LangGraph node responsible for answer generation.
    """

    def __init__(
        self,
        llm: BaseLLM,
    ):
        self._llm = llm
        self._logger = get_logger(
            self.__class__.__name__
        )

    def __call__(
        self,
        state: AgentState,
    ) -> AgentState:
        """
        Generate the final answer.
        """

        if state["context"]:

            prompt = RAG_PROMPT.format(
                context=state["context"],
                question=state["question"],
            )

        else:

            route = state["metadata"].get("route")

            if route == "generate":

                # Router intentionally skipped retrieval
                prompt = state["question"]

            else:

                # Retrieval failed to find relevant context
                prompt = """
No relevant documents were found in the knowledge base.

Respond exactly with:

"I don't know based on the provided documents."
"""

        answer = self._llm.generate(prompt)

        state["answer"] = answer

        state["metadata"].update(
            {
                "generator": type(self._llm).__name__,
            }
        )

        self._logger.info(
            "Response generated successfully."
        )
        return state