"""
Week 4 - Chunk Size and Overlap Experiment.

Reuses the FixedChunker and RecursiveChunker
implemented in Week 3.

The experiment compares different chunk sizes
and overlap values and reports:

- Number of chunks
- Average chunk length
- Minimum chunk length
- Maximum chunk length
- Processing time
"""

import os
import time

from week3.src.processing.fixed_chunker import FixedChunker
from week3.src.processing.recursive_chunker import RecursiveChunker


# ============================================================
# Configuration
# ============================================================

DOCUMENT_PATH = "week3/data/documents/Introduction to Database.pdf"

CONFIGURATIONS = [
    {"chunk_size": 300, "chunk_overlap": 30},
    {"chunk_size": 500, "chunk_overlap": 50},
    {"chunk_size": 800, "chunk_overlap": 80},
    {"chunk_size": 1000, "chunk_overlap": 100},
]


# ============================================================
# Load Document
# ============================================================

def load_document_text(path: str) -> str:
    """
    Read the document.

    This experiment focuses on chunk size and overlap,
    so we use plain text input rather than changing
    the Week 3 ingestion pipeline.
    """

    if not os.path.exists(path):
        raise FileNotFoundError(
            f"Document not found: {path}"
        )

    with open(
        path,
        "rb",
    ) as file:

        raw_data = file.read()

    # Basic PDF extraction without changing Week 3.
    try:

        from pypdf import PdfReader

        reader = PdfReader(path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)

    except ImportError:

        raise ImportError(
            "pypdf is required for this experiment. "
            "Install it using: pip install pypdf"
        )


# ============================================================
# Create Document Object
# ============================================================

def create_document(text: str):
    """
    Convert text into the LangChain Document type
    expected by the Week 3 chunkers.
    """

    from langchain_core.documents import Document

    return Document(
        page_content=text,
        metadata={
            "source": DOCUMENT_PATH,
        },
    )


# ============================================================
# Run Single Experiment
# ============================================================

def run_experiment(
    chunker_name: str,
    chunker,
    document,
    chunk_size: int,
    chunk_overlap: int,
):

    start_time = time.perf_counter()

    chunks = chunker.split_documents(
        [document]
    )

    elapsed = time.perf_counter() - start_time

    lengths = [
        len(chunk.page_content)
        for chunk in chunks
        if chunk.page_content
    ]

    if not lengths:

        return {
            "chunker": chunker_name,
            "chunk_size": chunk_size,
            "overlap": chunk_overlap,
            "num_chunks": 0,
            "avg_length": 0,
            "min_length": 0,
            "max_length": 0,
            "time_seconds": round(elapsed, 4),
        }

    return {
        "chunker": chunker_name,
        "chunk_size": chunk_size,
        "overlap": chunk_overlap,
        "num_chunks": len(chunks),
        "avg_length": round(
            sum(lengths) / len(lengths),
            2,
        ),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "time_seconds": round(
            elapsed,
            4,
        ),
    }


# ============================================================
# Run All Experiments
# ============================================================

def main():

    print("=" * 80)
    print("WEEK 4 - CHUNK SIZE & OVERLAP EXPERIMENT")
    print("=" * 80)

    print()
    print(f"Document: {DOCUMENT_PATH}")

    text = load_document_text(
        DOCUMENT_PATH
    )

    print(
        f"Document characters: {len(text)}"
    )

    document = create_document(text)

    results = []

    # --------------------------------------------------------
    # Fixed Chunker
    # --------------------------------------------------------

    for config in CONFIGURATIONS:

        chunker = FixedChunker(
            chunk_size=config["chunk_size"],
            chunk_overlap=config["chunk_overlap"],
        )

        result = run_experiment(
            chunker_name="Fixed",
            chunker=chunker,
            document=document,
            chunk_size=config["chunk_size"],
            chunk_overlap=config["chunk_overlap"],
        )

        results.append(result)

    # --------------------------------------------------------
    # Recursive Chunker
    # --------------------------------------------------------

    for config in CONFIGURATIONS:

        chunker = RecursiveChunker(
            chunk_size=config["chunk_size"],
            chunk_overlap=config["chunk_overlap"],
        )

        result = run_experiment(
            chunker_name="Recursive",
            chunker=chunker,
            document=document,
            chunk_size=config["chunk_size"],
            chunk_overlap=config["chunk_overlap"],
        )

        results.append(result)

    # --------------------------------------------------------
    # Display Results
    # --------------------------------------------------------

    print()
    print("-" * 80)

    header = (
        f"{'Chunker':<12}"
        f"{'Size':<10}"
        f"{'Overlap':<10}"
        f"{'Chunks':<10}"
        f"{'Avg Len':<12}"
        f"{'Min':<10}"
        f"{'Max':<10}"
        f"{'Time(s)':<10}"
    )

    print(header)
    print("-" * 80)

    for result in results:

        print(
            f"{result['chunker']:<12}"
            f"{result['chunk_size']:<10}"
            f"{result['overlap']:<10}"
            f"{result['num_chunks']:<10}"
            f"{result['avg_length']:<12}"
            f"{result['min_length']:<10}"
            f"{result['max_length']:<10}"
            f"{result['time_seconds']:<10}"
        )

    print("-" * 80)

    # --------------------------------------------------------
    # Save Results
    # --------------------------------------------------------

    output_directory = "week4/evaluation"

    os.makedirs(
        output_directory,
        exist_ok=True,
    )

    output_file = (
        f"{output_directory}/"
        "chunking_experiment_results.csv"
    )

    with open(
        output_file,
        "w",
        encoding="utf-8",
    ) as file:

        file.write(
            "chunker,chunk_size,overlap,"
            "num_chunks,avg_length,min_length,"
            "max_length,time_seconds\n"
        )

        for result in results:

            file.write(
                f"{result['chunker']},"
                f"{result['chunk_size']},"
                f"{result['overlap']},"
                f"{result['num_chunks']},"
                f"{result['avg_length']},"
                f"{result['min_length']},"
                f"{result['max_length']},"
                f"{result['time_seconds']}\n"
            )

    print()
    print(
        f"Results saved to: {output_file}"
    )


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()