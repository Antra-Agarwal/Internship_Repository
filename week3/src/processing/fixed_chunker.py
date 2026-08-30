"""
Fixed-size document chunking.
"""

from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

from src.processing.base_chunker import BaseChunker
from src.processing.metadata import add_chunk_metadata


class FixedChunker(BaseChunker):
    """
    Splits documents into fixed-size chunks.

    CharacterTextSplitter is used to create chunks while
    maintaining configurable overlap between neighbouring chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separator: str = "\n",
    ):
        """
        Initialize the fixed chunker.

        Args:
            chunk_size:
                Maximum chunk size.

            chunk_overlap:
                Number of overlapping characters.

            separator:
                Preferred split separator.
        """

        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than zero."
            )

        if chunk_overlap < 0:
            raise ValueError(
                "chunk_overlap cannot be negative."
            )

        if chunk_overlap >= chunk_size:
            raise ValueError(
                "chunk_overlap must be smaller than chunk_size."
            )

        self._text_splitter = CharacterTextSplitter(
            separator=separator,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split documents into fixed-size chunks.

        Args:
            documents:
                List of LangChain Document objects.

        Returns:
            List of chunked documents with standardized metadata.
        """

        if not documents:
            return []

        chunks = self._text_splitter.split_documents(
            documents
        )

        return add_chunk_metadata(
            chunks,
            strategy="fixed",
        )