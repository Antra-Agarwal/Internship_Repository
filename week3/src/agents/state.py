"""
Shared state for the LangGraph RAG Agent.
"""

from typing import Any, TypedDict

from src.vectorstores.base import SearchResult


class AgentState(TypedDict):
    """
    Shared state passed between LangGraph nodes.

    Each node reads the current state, updates the fields
    it is responsible for, and returns the updated state.
    """

    # Original user question
    question: str

    # Retrieved search results
    results: list[SearchResult]

    # Combined context from retrieved documents
    context: str

    # Final generated answer
    answer: str

    # Execution metadata
    metadata: dict[str, Any]