"""
Shared state for the LangGraph RAG Agent.
"""

from typing import Any, TypedDict

from src.vectorstores.base import SearchResult


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.

    Every node reads this state, updates the fields
    it is responsible for, and returns the updated state.
    """

    # User's question
    question: str

    # Retrieved search results
    results: list[SearchResult]

    # Combined document context
    context: str

    # Final answer
    answer: str

    # Execution metadata
    metadata: dict[str, Any]