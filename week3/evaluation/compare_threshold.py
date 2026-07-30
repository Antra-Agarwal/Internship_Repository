"""
Compare retrieval quality using different similarity thresholds.
"""

import time

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.retrievers.vectorstore_retriever import VectorStoreRetriever
from src.vectorstores.faiss_store import FAISSVectorStore


# Since we are using L2 distance,
# smaller distance means better similarity.
THRESHOLDS = [
    0.55,
    0.60,
    0.65,
    0.70,
]


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

    print("\nSample Metadata:")
    print(vector_store._documents[0].metadata)
    print()

    retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    print("=" * 70)
    print("SIMILARITY THRESHOLD COMPARISON")
    print("=" * 70)

    while True:

        query = input("\nEnter query (or 'exit'): ").strip()

        if query.lower() == "exit":
            break

        if not query:
            continue

        for threshold in THRESHOLDS:

            print()
            print("=" * 70)
            print(f"Maximum Distance = {threshold}")
            print("=" * 70)

            start = time.perf_counter()

            results = retriever.retrieve(
                query=query,
                k=10,
                max_distance=threshold,
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