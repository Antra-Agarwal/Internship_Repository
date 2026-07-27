"""
Integration test for the document chunking pipeline.
"""

from pathlib import Path

from src.loaders import DocumentLoaderManager
from src.processing.document_processor import DocumentProcessor
from src.processing.fixed_chunker import FixedChunker


DOCUMENTS_DIR = Path("data/documents")


def load_documents():
    """
    Load all supported documents.
    """

    print("\nLoading documents...")

    manager = DocumentLoaderManager()

    documents = manager.load_directory(
        str(DOCUMENTS_DIR)
    )

    print(f"Loaded {len(documents)} document(s).")

    return documents


def process_documents(documents):
    """
    Split documents into chunks.
    """

    print("\nProcessing documents...")

    processor = DocumentProcessor(
        FixedChunker()
    )

    chunks = processor.process_documents(
        documents
    )

    print(f"Generated {len(chunks)} chunk(s).")

    return chunks


def display_sample_chunk(chunks):
    """
    Display the first chunk.
    """

    first_chunk = chunks[0]

    print("\nFirst Chunk Preview")
    print("-" * 60)
    print(first_chunk.page_content[:300])

    print("\nMetadata")
    print("-" * 60)
    print(first_chunk.metadata)


def main():

    print("=" * 60)
    print("DOCUMENT CHUNKING TEST")
    print("=" * 60)

    documents = load_documents()

    chunks = process_documents(
        documents
    )

    display_sample_chunk(
        chunks
    )

    print("\n" + "=" * 60)
    print("TEST PASSED")
    print("=" * 60)


if __name__ == "__main__":
    main()