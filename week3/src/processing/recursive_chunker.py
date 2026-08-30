"""
Recursive document chunking.
"""

from langchain_core.documents import Document
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

from src.processing.base_chunker import BaseChunker
from src.processing.metadata import add_chunk_metadata


class RecursiveChunker(BaseChunker):
    """
    Splits documents recursively using increasingly smaller
    separators while preserving semantic structure where possible.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        """
        Initialize the recursive chunker.

        Args:
            chunk_size:
                Maximum chunk size.

            chunk_overlap:
                Number of overlapping characters.
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

        self._text_splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap,
            )
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split documents recursively.

        Args:
            documents:
                List of LangChain Document objects.

        Returns:
            Chunked documents with standardized metadata.
        """

        if not documents:
            return []

        try:

            chunks = self._text_splitter.split_documents(
                documents
            )

            return add_chunk_metadata(
                chunks,
                strategy="recursive",
            )

        except Exception as error:

            raise RuntimeError(
                "Failed to split documents into chunks."
            ) from error