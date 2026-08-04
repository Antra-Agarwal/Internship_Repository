"""
Routing logic for the LangGraph agent.
"""

from .state import AgentState


class RouterNode:
    """
    Decides whether retrieval is required.

    Returns:
        "retrieve" -> Retrieve documents first.
        "generate" -> Skip retrieval.
    """

    GREETINGS = {
        "hi",
        "hello",
        "hey",
        "good morning",
        "good evening",
        "thanks",
        "thank you",
        "bye",
    }

    def __call__(
        self,
        state: AgentState,
    ) -> str:

        question = state["question"].lower().strip()

        if question in self.GREETINGS:
            return "generate"

        return "retrieve"