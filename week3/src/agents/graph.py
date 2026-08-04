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

    def __init__(
        self,
        retriever: BaseRetriever,
        llm: BaseLLM,
        reranker: BaseReranker | None = None,
        retrieval_k: int = 10,
        final_k: int = 3,
    ):

        workflow = StateGraph(AgentState)

        workflow.add_node(
            "retrieve",
            RetrievalNode(
                retriever,
                reranker,
                retrieval_k,
                final_k,
            ),
        )

        workflow.add_node(
            "generate",
            GenerationNode(
                llm,
            ),
        )

        router = RouterNode()

        workflow.add_conditional_edges(
            START,
            router,
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

        initial_state: AgentState = {
            "question": question,
            "results": [],
            "context": "",
            "answer": "",
            "metadata": {},
        }

        return self._graph.invoke(initial_state)