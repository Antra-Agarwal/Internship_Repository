from typing import List
from src.processing.base_chunker import BaseChunker
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


class RecursiveChunker(BaseChunker):
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:
        try:
            chunks = self.text_splitter.split_documents(documents)
            return chunks

        except Exception as e:
            raise RuntimeError("Failed to split documents into chunks.") from e