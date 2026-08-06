"""
Google Gemini LLM implementation.
"""

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)
from langchain_google_genai.chat_models import (
    ChatGoogleGenerativeAIError,
)

from src.config import (
    GOOGLE_API_KEY,
    LLM_MODEL,
)
from src.llms.base_llm import BaseLLM
from src.utils.logger import get_logger


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

        self._logger = get_logger(
            self.__class__.__name__
        )

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

        try:

            response = self._llm.invoke(
                prompt
            )

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
                            block.get(
                                "text",
                                "",
                            )
                        )

                return (
                    "\n".join(text_parts)
                    .strip()
                )

            return str(content).strip()

        except ChatGoogleGenerativeAIError as error:

            self._logger.error(error)

            message = str(error)

            if (
                "RESOURCE_EXHAUSTED"
                in message
            ):

                return (
                    "The Gemini API quota has been exceeded.\n"
                    "Please try again later."
                )

            return (
                "The language model is currently unavailable.\n"
                "Please try again later."
            )

        except Exception as error:

            self._logger.exception(error)

            return (
                "An unexpected error occurred while "
                "generating the response."
            )