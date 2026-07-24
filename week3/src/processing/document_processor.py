from langchain_core.documents import Document

from src.processing.base_chunker import BaseChunker


class DocumentProcessor:
    """
    Coordinates the document preprocessing pipeline.

    Responsibilities:
    - Validate loaded documents
    - Delegate chunking to DocumentChunker
    - Return processed document chunks.
    """

    def __init__(self, chunker: BaseChunker):
        """
        Initialize the document processor.

        Args:
            chunker: Instance of BaseChunker used to split documents.
        """
        self._chunker = chunker

    def process_documents(
        self,
        documents: list[Document]
    ) -> list[Document]:
        """
        Process loaded documents into chunks.

        Args:
            documents: List of LangChain Document objects.

        Returns:
            List of chunked Document objects.
        """

        if not isinstance(documents, list):
            raise TypeError("documents must be a list of Document objects.")

        if not documents:
            raise ValueError("No documents provided for processing.")

        if not all(isinstance(doc, Document) for doc in documents):
            raise TypeError("All items must be LangChain Document objects.")

        chunks = self._chunker.split_documents(documents)

        print("\n========== Document Processing ==========")
        print(f"Input documents : {len(documents)}")
        print(f"Output chunks   : {len(chunks)}")
        print("=========================================\n")

        return chunks