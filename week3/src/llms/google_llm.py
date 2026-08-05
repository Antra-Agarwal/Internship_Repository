"""
Google Gemini LLM implementation.
"""

from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
)
from src.llms.base_llm import BaseLLM


class GoogleLLM(BaseLLM):
    """
    Google Gemini implementation of the BaseLLM interface.
    """

    def __init__(
        self,
        model: str = LLM_MODEL,
        temperature: float = 0.2,
    ):
        """
        Initialize the Gemini chat model.

        Args:
            model:
                Gemini model name.

            temperature:
                Sampling temperature.
        """

        self._llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=GOOGLE_API_KEY,
            temperature=temperature,
        )

    def generate(
            self,
            prompt: str,
    ) -> str:
        """
        Generate a response from Gemini.
        
        Args:
            prompt:
                Input prompt.
        Returns:
            Generated text.
        """

        response = self._llm.invoke(prompt)

        content = response.content

        # Gemini 3.x may return structured content blocks
        if isinstance(content, list):
            text_parts = []

            for block in content:
                if (
                    isinstance(block, dict)
                    and block.get("type") == "text"
                ):
                    text_parts.append(
                        block.get("text", "")
                    )

            return "\n".join(text_parts).strip()
        return str(content).strip()