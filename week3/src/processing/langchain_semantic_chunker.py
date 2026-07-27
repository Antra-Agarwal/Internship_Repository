from typing import List

from langchain_core.documents import Document
from langchain_experimental.text_splitter import SemanticChunker

from src.embeddings.base_embedding import BaseEmbedding
from src.processing.base_semantic_chunker import BaseSemanticChunker


_CHUNKING_STRATEGY = "langchain_semantic"


class LangChainSemanticChunker(BaseSemanticChunker):
    """
    Wrapper around LangChain's SemanticChunker.
    """

    def __init__(
        self,
        embedding_model: BaseEmbedding,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        super().__init__(
            embedding_model=embedding_model,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        self._semantic_chunker = SemanticChunker(
            embeddings=self.embedding_model.embedding_client
        )

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:

        chunks = self._semantic_chunker.split_documents(
            documents
        )

        for index, chunk in enumerate(chunks):

            metadata = chunk.metadata.copy()

            metadata["chunk_index"] = index
            metadata["chunking_strategy"] = _CHUNKING_STRATEGY

            chunk.metadata = metadata

        return chunks