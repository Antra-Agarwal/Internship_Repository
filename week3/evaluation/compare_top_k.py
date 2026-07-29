"""
Compare retrieval quality for different Top-K values.
"""

import time

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.retrievers.vectorstore_retriever import VectorStoreRetriever
from src.vectorstores.faiss_store import FAISSVectorStore


TOP_K_VALUES = [1, 3, 5, 10]


def print_result(rank, result):
    """
    Pretty-print a search result.
    """

    document = result.document
    metadata = document.metadata

    print("-" * 70)
    print(f"Rank       : {rank}")
    print(f"Distance   : {result.score:.4f}")
    print(f"Source     : {metadata.get('source', 'Unknown')}")
    print(f"Page       : {metadata.get('page', '-')}")
    print(f"Chunk Size : {len(document.page_content)} characters")

    preview = (
        document.page_content[:200]
        .replace("\n", " ")
        .strip()
    )

    print(f"Preview    : {preview}...")
    print()


def main():

    load_dotenv()

    embedding_model = GoogleEmbeddingModel()

    vector_store = FAISSVectorStore()
    vector_store.load("data/vector_db")

    retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    print("=" * 70)
    print("TOP-K RETRIEVAL COMPARISON")
    print("=" * 70)

    while True:

        query = input("\nEnter query (or 'exit'): ").strip()

        if query.lower() == "exit":
            break

        if not query:
            continue

        for k in TOP_K_VALUES:

            print()
            print("=" * 70)
            print(f"Top-K = {k}")
            print("=" * 70)

            start = time.perf_counter()

            results = retriever.retrieve(
                query=query,
                k=k,
            )

            elapsed = time.perf_counter() - start

            print(f"Retrieved : {len(results)} document(s)")
            print(f"Time      : {elapsed:.4f} seconds")
            print()

            for rank, result in enumerate(
                results,
                start=1,
            ):
                print_result(rank, result)


if __name__ == "__main__":
    main()