from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import src.config

from src.embeddings.base_embedding import BaseEmbedding


class GoogleEmbeddingModel(BaseEmbedding):
    """
    Google Gemini embedding model implementation.
    """

    def __init__(
        self,
        model_name: str = "models/gemini-embedding-001"
    ):
        """
        Initialize the Google embedding model.

        Args:
            model_name: Google embedding model to use.
        """
        self._embedding_model = GoogleGenerativeAIEmbeddings(
            model=model_name
        )

    def embed_documents(
        self,
        documents: list[Document]
    ) -> list[list[float]]:
        """
        Generate embeddings for a list of documents.

        Args:
            documents: List of LangChain Document objects.

        Returns:
            List of embedding vectors.
        """
        texts = [
            document.page_content
            for document in documents
        ]

        return self._embedding_model.embed_documents(texts)

    def embed_query(
        self,
        query: str
    ) -> list[float]:
        """
        Generate an embedding for a user query.

        Args:
            query: User query.

        Returns:
            Embedding vector.
        """
        return self._embedding_model.embed_query(query)