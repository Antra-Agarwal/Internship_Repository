from pathlib import Path
from statistics import mean
from typing import Any

from langchain_core.documents import Document

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.loaders.document_loader_manager import DocumentLoaderManager
from src.processing.custom_semantic_chunker import CustomSemanticChunker
from src.processing.fixed_chunker import FixedChunker
from src.processing.langchain_semantic_chunker import LangChainSemanticChunker
from src.processing.recursive_chunker import RecursiveChunker
from src.processing.semantic_similarity import AdjacentSimilarityStrategy


# ==========================================================
# Chunking Configuration
# ==========================================================

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
SIMILARITY_THRESHOLD = 0.80


# ==========================================================
# Shared Objects
# ==========================================================

_loader_manager = DocumentLoaderManager()

_embedding_model = GoogleEmbeddingModel()

_similarity_strategy = AdjacentSimilarityStrategy()


# ==========================================================
# Document Loading
# ==========================================================

def load_documents(path: str) -> list[Document]:
    """
    Load a supported file or an entire directory.
    """

    path = Path(path)

    if path.is_dir():
        return _loader_manager.load_directory(str(path))

    return _loader_manager.load_file(str(path))


# ==========================================================
# Chunker Factory
# ==========================================================

def create_chunkers() -> list[tuple[str, Any]]:
    """
    Create all available chunkers.
    """

    return [
        (
            "Fixed Chunker",
            FixedChunker(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
            ),
        ),
        (
            "Recursive Chunker",
            RecursiveChunker(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
            ),
        ),
        (
            "Custom Semantic Chunker",
            CustomSemanticChunker(
                embedding_model=_embedding_model,
                similarity_strategy=_similarity_strategy,
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                similarity_threshold=SIMILARITY_THRESHOLD,
            ),
        ),
        (
            "LangChain Semantic Chunker",
            LangChainSemanticChunker(
                embedding_model=_embedding_model,
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
            ),
        ),
    ]


# ==========================================================
# Statistics
# ==========================================================

def get_chunk_statistics(chunks: list[Document]) -> dict | None:
    """
    Compute statistics for generated chunks.
    """

    if not chunks:
        return None

    chunk_lengths = [
        len(chunk.page_content)
        for chunk in chunks
    ]

    return {
        "chunks_created": len(chunks),
        "average_length": mean(chunk_lengths),
        "smallest_chunk": min(chunk_lengths),
        "largest_chunk": max(chunk_lengths),
    }


# ==========================================================
# Printing Utilities
# ==========================================================

def print_separator(length: int = 80) -> None:
    print("=" * length)


def print_chunk_statistics(
    name: str,
    stats: dict | None,
) -> None:

    print_separator()

    print(name.upper())

    print_separator()

    if stats is None:
        print("No chunks generated.\n")
        return

    print(f"Chunks Created : {stats['chunks_created']}")
    print(f"Average Length : {stats['average_length']:.2f}")
    print(f"Smallest Chunk : {stats['smallest_chunk']}")
    print(f"Largest Chunk  : {stats['largest_chunk']}")

    print()


def print_chunk_preview(
    chunks: list[Document],
    preview_length: int = 400,
) -> None:

    if not chunks:
        return

    print("FIRST CHUNK")
    print("-" * 80)

    preview = chunks[0].page_content[:preview_length]

    if len(chunks[0].page_content) > preview_length:
        preview += "..."

    print(preview)
    print()


def print_metadata(chunks: list[Document]) -> None:

    if not chunks:
        return

    print("METADATA")
    print("-" * 80)

    for key, value in chunks[0].metadata.items():
        print(f"{key}: {value}")

    print()


def print_results(
    name: str,
    chunks: list[Document],
) -> None:

    stats = get_chunk_statistics(chunks)

    print_chunk_statistics(name, stats)

    print_chunk_preview(chunks)

    print_metadata(chunks)