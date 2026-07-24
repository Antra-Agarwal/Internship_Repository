from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BaseChunker(ABC):
    """
    Abstract base class for all document chunking strategies.
    """

    @abstractmethod
    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Split documents into smaller chunks.

        Args:
            documents: List of LangChain Document objects.

        Returns:
            List of chunked Document objects.
        """
        pass