"""
Tool Executor.

Responsible for:
1. Selecting the appropriate tool.
2. Executing the selected tool.
"""

import re

from .registry import ToolRegistry


class ToolExecutor:
    """
    Executes the appropriate tool for a user query.
    """

    def __init__(
        self,
        registry: ToolRegistry,
    ):
        self._registry = registry

    def execute(
        self,
        query: str,
    ) -> str | None:
        """
        Execute a tool if the query matches one.

        Args:
            query:
                User query.

        Returns:
            Tool result if executed, otherwise None.
        """

        query = query.strip()

        # -------------------------
        # Calculator Tool
        # -------------------------

        if self._is_math_expression(query):

            tool = self._registry.get("calculator")

            if tool is not None:
                return tool.run(query)

        # -------------------------
        # File Reader Tool
        # -------------------------

        if query.lower().startswith(
            (
                "read ",
                "open ",
                "show ",
            )
        ):

            path = (
                query.replace("read", "")
                .replace("open", "")
                .replace("show", "")
                .strip()
            )

            tool = self._registry.get("file_reader")

            if tool is not None:
                return tool.run(path)

        return None

    @staticmethod
    def _is_math_expression(
        text: str,
    ) -> bool:
        """
        Check whether the input looks like a
        mathematical expression.
        """

        pattern = r"^[0-9+\-*/().%\s]+$"

        return bool(
            re.fullmatch(
                pattern,
                text,
            )
        )