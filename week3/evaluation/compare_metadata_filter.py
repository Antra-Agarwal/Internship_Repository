"""
Compare retrieval using metadata filtering.
"""

import time
from pathlib import Path

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.retrievers.vectorstore_retriever import VectorStoreRetriever
from src.vectorstores.faiss_store import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"


def print_result(rank, result):
    """
    Print a search result.
    """

    document = result.document
    metadata = document.metadata

    print("-" * 70)
    print(f"Rank       : {rank}")
    print(f"Distance   : {result.score:.4f}")
    print(f"Source     : {metadata.get('source')}")
    print(f"Page       : {metadata.get('page')}")

    preview = (
        document.page_content[:200]
        .replace("\n", " ")
        .strip()
    )

    print(f"Preview    : {preview}...")
    print()


def get_document_sources(vector_store):
    """
    Return all unique document sources.
    """

    sources = sorted(
        {
            document.metadata["source"]
            for document in vector_store._documents
        }
    )

    return sources


def choose_source(sources):
    """
    Let the user choose a document to search.
    """

    print("\nAvailable Documents")
    print("=" * 70)
    print("0. All Documents")

    for index, source in enumerate(sources, start=1):
        filename = Path(source).name
        print(f"{index}. {filename}")

    while True:

        choice = input("\nChoose a document: ").strip()

        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        if 0 <= choice <= len(sources):
            break

        print("Invalid selection.")

    if choice == 0:
        return None

    return sources[choice - 1]


def main():

    load_dotenv()

    embedding_model = GoogleEmbeddingModel()

    vector_store = FAISSVectorStore()
    vector_store.load(VECTOR_DB_PATH)

    retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    sources = get_document_sources(vector_store)

    print("=" * 70)
    print("METADATA FILTERING")
    print("=" * 70)

    selected_source = choose_source(sources)

    if selected_source is None:
        print("\nSearch Mode : All Documents")
        metadata_filter = None
    else:
        print(f"\nSearch Mode : {Path(selected_source).name}")
        metadata_filter = {
            "source": selected_source,
        }

    while True:

        query = input("\nEnter query (or 'exit'): ").strip()

        if query.lower() == "exit":
            break

        start = time.perf_counter()

        results = retriever.retrieve(
            query=query,
            k=5,
            metadata_filter=metadata_filter,
        )

        elapsed = time.perf_counter() - start

        print(f"\nRetrieved : {len(results)} document(s)")
        print(f"Time      : {elapsed:.4f} seconds\n")

        if not results:
            print("No matching documents found.\n")
            continue

        for rank, result in enumerate(results, start=1):
            print_result(rank, result)


if __name__ == "__main__":
    main()