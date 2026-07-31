"""
Compare Dense, BM25 and Hybrid Retrieval.
"""

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever
from src.retrievers.vectorstore_retriever import VectorStoreRetriever
from src.vectorstores.faiss_store import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"


def print_results(title, results):
    """
    Print retrieval results.
    """

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    if not results:
        print("No results found.")
        return

    for i, result in enumerate(results, start=1):

        source = result.document.metadata.get(
            "source",
            "Unknown",
        )

        preview = result.document.page_content[:150]
        preview = preview.replace("\n", " ")

        print(f"\n{i}. Score : {result.score:.4f}")
        print(f"Source    : {source}")
        print(f"Content   : {preview}...")


def main():

    load_dotenv()

    embedding_model = GoogleEmbeddingModel()

    vector_store = FAISSVectorStore()
    vector_store.load(VECTOR_DB_PATH)

    dense = VectorStoreRetriever(
        vector_store=vector_store,
        embedding_model=embedding_model,
    )

    bm25 = BM25Retriever(
        vector_store=vector_store,
    )

    hybrid = HybridRetriever(
        vector_retriever=dense,
        bm25_retriever=bm25,
    )

    print("=" * 70)
    print("HYBRID SEARCH COMPARISON (RRF)")
    print("=" * 70)

    while True:

        query = input(
            "\nEnter query (or 'exit'): "
        ).strip()

        if query.lower() == "exit":
            break

        try:
            k = int(
                input(
                    "Top-k (default 5): "
                )
                or 5
            )

            if k <= 0:
                raise ValueError

        except ValueError:

            print("Please enter a positive integer.")
            continue

        dense_results = dense.retrieve(
            query=query,
            k=k,
        )

        bm25_results = bm25.retrieve(
            query=query,
            k=k,
        )

        hybrid_results = hybrid.retrieve(
            query=query,
            k=k,
        )

        print_results(
            "DENSE RETRIEVAL",
            dense_results,
        )

        print_results(
            "BM25 RETRIEVAL",
            bm25_results,
        )

        print_results(
            "HYBRID RETRIEVAL (RRF)",
            hybrid_results,
        )


if __name__ == "__main__":
    main()