"""
Abstract base class for all agent tools.
"""

from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseTool(ABC):
    """
    Base class for all tools.
    """

    @property
    @abstractmethod
    def name(self) -> str:
        """
        Unique tool name.
        """

    @property
    @abstractmethod
    def description(self) -> str:
        """
        Tool description used by the agent.
        """

    @abstractmethod
    def run(
        self,
        input_data: str,
    ) -> Any:
        """
        Execute the tool.
        """