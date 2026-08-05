"""
Short-term conversation memory.
"""

from collections import deque


class ConversationMemory:
    """
    Stores recent conversation history.
    """

    def __init__(
        self,
        max_turns: int = 5,
    ):
        self._history = deque(maxlen=max_turns * 2)

    def add_user_message(
        self,
        message: str,
    ) -> None:

        self._history.append(
            ("User", message)
        )

    def add_assistant_message(
        self,
        message: str,
    ) -> None:

        self._history.append(
            ("Assistant", message)
        )

    def get_history(self) -> str:
        """
        Return formatted conversation history.
        """

        if not self._history:
            return ""

        return "\n".join(
            f"{role}: {message}"
            for role, message in self._history
        )

    def clear(self) -> None:

        self._history.clear()