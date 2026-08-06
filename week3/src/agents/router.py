"""
LLM-powered router for the LangGraph agent.
"""

from src.llms import BaseLLM
from src.prompts.router_prompt import ROUTER_PROMPT
from src.utils.logger import get_logger

from .state import AgentState


class RouterNode:
    """
    LangGraph routing node.

    Uses an LLM to decide whether the user's question
    requires document retrieval.

    Returns:
        "retrieve" -> Execute RetrievalNode
        "generate" -> Skip retrieval and generate directly
    """

    VALID_ROUTES = {
        "retrieve",
        "generate",
    }

    def __init__(
        self,
        llm: BaseLLM,
    ):
        """
        Initialize the router.

        Args:
            llm:
                LLM used for routing decisions.
        """

        self._llm = llm
        self._logger = get_logger(
            self.__class__.__name__
        )

    def __call__(
            self,
            state: AgentState,
    ) -> str:
        """
        Decide which path the graph should follow.
        Args:
            state:
            Current graph state.
        Returns:
            Graph route.
        """

        prompt = ROUTER_PROMPT.format(
            question=state["question"],
        )

        response = self._llm.generate(prompt)
        tokens = response.strip().lower().split()

        decision = (
            tokens[0]
            if tokens
            else "retrieve"
        )

        # Remove trailing punctuation if the LLM returns
        # values such as "retrieve." or "generate,"
        decision = decision.rstrip(".,:;!?")

        if decision not in self.VALID_ROUTES:
            decision = "retrieve"

        state["metadata"]["route"] = decision
        self._logger.info(
            f"Route selected: {decision}"
        )
        return decision