from langchain_text_splitters import CharacterTextSplitter
from langchain_core.documents import Document

from src.processing.base_chunker import BaseChunker


class FixedChunker(BaseChunker):
    """
    Splits documents into fixed-size chunks using CharacterTextSplitter.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separator: str = "\n"
    ):
        self._text_splitter = CharacterTextSplitter(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

    def split_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Split documents into fixed-size chunks.

        Args:
            documents: List of LangChain Document objects.

        Returns:
            List of chunked documents.
        """
        return self._text_splitter.split_documents(documents)