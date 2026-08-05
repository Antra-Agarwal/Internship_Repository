"""
LangGraph workflow for the RAG Agent.
"""

from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from src.llms import BaseLLM
from src.rerankers import BaseReranker
from src.retrievers import BaseRetriever

from .nodes import GenerationNode
from .nodes import RetrievalNode
from .router import RouterNode
from .state import AgentState


class RAGAgent:
    """
    LangGraph implementation of a Retrieval-Augmented
    Generation (RAG) Agent.

    Workflow:

        START
           │
           ▼
      RouterNode
       /       \
      /         \
 retrieve     generate
      │            │
      ▼            │
 RetrievalNode     │
      │            │
      └──────┬─────┘
             ▼
      GenerationNode
             │
             ▼
            END
    """

    def __init__(
        self,
        retriever: BaseRetriever,
        router_llm: BaseLLM,
        generator_llm: BaseLLM,
        reranker: BaseReranker | None = None,
        retrieval_k: int = 10,
        final_k: int = 3,
        rerank_threshold: float = 0.0,
    ):
        """
        Initialize the LangGraph workflow.

        Args:
            retriever:
                Document retriever.

            router_llm:
                LLM used for routing decisions.

            generator_llm:
                LLM used for answer generation.

            reranker:
                Optional reranker.

            retrieval_k:
                Number of documents retrieved before reranking.

            final_k:
                Number of documents kept after reranking.

            rerank_threshold:
                Minimum reranker score required for
                retrieved documents to be considered relevant.
        """

        self._retriever = retriever
        self._router_llm = router_llm
        self._generator_llm = generator_llm
        self._reranker = reranker
        self._rerank_threshold = rerank_threshold

        workflow = StateGraph(AgentState)

        router_node = RouterNode(
            llm=self._router_llm,
        )

        retrieval_node = RetrievalNode(
            retriever=self._retriever,
            reranker=self._reranker,
            retrieval_k=retrieval_k,
            final_k=final_k,
            rerank_threshold=self._rerank_threshold,
        )

        generation_node = GenerationNode(
            llm=self._generator_llm,
        )

        workflow.add_node(
            "retrieve",
            retrieval_node,
        )

        workflow.add_node(
            "generate",
            generation_node,
        )

        workflow.add_conditional_edges(
            START,
            router_node,
            {
                "retrieve": "retrieve",
                "generate": "generate",
            },
        )

        workflow.add_edge(
            "retrieve",
            "generate",
        )

        workflow.add_edge(
            "generate",
            END,
        )

        self._graph = workflow.compile()

    def invoke(
        self,
        question: str,
    ) -> AgentState:
        """
        Execute the LangGraph workflow.

        Args:
            question:
                User question.

        Returns:
            Final graph state.
        """

        initial_state: AgentState = {
            "question": question,
            "results": [],
            "context": "",
            "answer": "",
            "metadata": {},
        }

        return self._graph.invoke(initial_state)