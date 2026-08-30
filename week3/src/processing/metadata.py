"""
Utilities for standardizing document chunk metadata.
"""

from langchain_core.documents import Document


def add_chunk_metadata(
    documents: list[Document],
    strategy: str,
) -> list[Document]:
    """
    Add standardized metadata to document chunks.

    Args:
        documents:
            Chunked LangChain Document objects.

        strategy:
            Name of the chunking strategy.

    Returns:
        Documents with standardized chunk metadata.
    """

    chunked_documents: list[Document] = []

    for index, document in enumerate(documents):

        metadata = document.metadata.copy()

        metadata["chunk_index"] = index
        metadata["chunking_strategy"] = strategy

        chunked_documents.append(
            Document(
                page_content=document.page_content,
                metadata=metadata,
            )
        )

    return chunked_documents