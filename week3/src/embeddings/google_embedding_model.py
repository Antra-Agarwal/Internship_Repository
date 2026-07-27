from langchain_google_genai import GoogleGenerativeAIEmbeddings

from src.config import EMBEDDING_MODEL, GOOGLE_API_KEY
from src.embeddings.base_embedding import BaseEmbedding


class GoogleEmbeddingModel(BaseEmbedding):
    """
    Google Gemini embedding model implementation.
    """

    def __init__(self):
        self._embeddings = GoogleGenerativeAIEmbeddings(
            model=EMBEDDING_MODEL,
            google_api_key=GOOGLE_API_KEY,
        )

    @property
    def embedding_client(self):
        """
        Return the underlying LangChain embedding client.
        """
        return self._embeddings

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:
        """
        Generate embeddings for multiple texts.
        """
        return self._embeddings.embed_documents(texts)

    def embed_query(
        self,
        query: str,
    ) -> list[float]:
        """
        Generate an embedding for a query.
        """
        return self._embeddings.embed_query(query)