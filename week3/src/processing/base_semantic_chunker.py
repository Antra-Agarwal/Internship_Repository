from abc import abstractmethod

from langchain_core.documents import Document

from src.embeddings.base_embedding import BaseEmbedding
from src.processing.base_chunker import BaseChunker


class BaseSemanticChunker(BaseChunker):
    """
    Base class for semantic chunking implementations.

    Stores common configuration shared by all semantic chunkers,
    including the embedding model and chunk size settings.
    """

    def __init__(
        self,
        embedding_model: BaseEmbedding,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self._embedding_model = embedding_model
        self._chunk_size = chunk_size
        self._chunk_overlap = chunk_overlap

    @property
    def embedding_model(self) -> BaseEmbedding:
        """
        Return the embedding model used for semantic similarity.
        """
        return self._embedding_model

    @property
    def chunk_size(self) -> int:
        """
        Maximum size of a chunk (characters).
        """
        return self._chunk_size

    @property
    def chunk_overlap(self) -> int:
        """
        Number of overlapping characters between chunks.
        """
        return self._chunk_overlap

    @abstractmethod
    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:
        """
        Split documents into semantic chunks.

        Must be implemented by subclasses.
        """
        pass