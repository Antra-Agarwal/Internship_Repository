from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import GOOGLE_API_KEY
from src.llms.base_llm import BaseLLM


class GoogleLLM(BaseLLM):
    """
    Google Gemini implementation.
    """

    def __init__(
        self,
        model: str = "gemini-2.5-flash",
        temperature: float = 0.2,
    ):

        self._llm = ChatGoogleGenerativeAI(
            model=model,
            google_api_key=GOOGLE_API_KEY,
            temperature=temperature,
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self._llm.invoke(prompt)

        return response.content