from abc import ABC, abstractmethod


class BaseLLM(ABC):
    """
    Abstract base class for all LLMs.
    """

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response from the LLM.

        Args:
            prompt: Input prompt.

        Returns:
            Generated response.
        """
        pass