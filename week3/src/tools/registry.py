"""
Tool registry.
"""

from .base_tool import BaseTool


class ToolRegistry:
    """
    Registry containing all available tools.
    """

    def __init__(self):

        self._tools: dict[str, BaseTool] = {}

    def register(
        self,
        tool: BaseTool,
    ) -> None:

        self._tools[tool.name] = tool

    def get(
        self,
        name: str,
    ) -> BaseTool | None:

        return self._tools.get(name)

    def list_tools(
        self,
    ) -> list[BaseTool]:

        return list(self._tools.values())