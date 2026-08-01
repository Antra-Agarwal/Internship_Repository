"""
Compare retrieval before and after reranking.
"""

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.rerankers import CrossEncoderReranker
from src.retrievers.vectorstore_retriever import (
    VectorStoreRetriever,
)
from src.vectorstores.faiss_store import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"


def print_results(
    title,
    results,
):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)

    if not results:
        print("No results.")
        return

    for i, result in enumerate(
        results,
        start=1,
    ):

        print(f"\nRank : {i}")
        print(f"Cross-Encoder Score : {result.score:.4f}")
        print(
            "Source:",
            result.document.metadata.get(
                "source",
                "Unknown",
            ),
        )

        preview = (
            result.document.page_content[:150]
            .replace("\n", " ")
        )

        print(preview + "...")


def main():

    load_dotenv()

    embedding_model = GoogleEmbeddingModel()

    vector_store = FAISSVectorStore()

    vector_store.load(
        VECTOR_DB_PATH
    )

    retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    reranker = CrossEncoderReranker()

    print("=" * 70)
    print("RERANKING COMPARISON")
    print("=" * 70)

    while True:

        query = input(
            "\nEnter query (or exit): "
        ).strip()

        if query.lower() == "exit":
            break

        retrieved = retriever.retrieve(
            query=query,
            k=10,
        )

        reranked = reranker.rerank(
            query=query,
            results=retrieved,
            top_k=5,
        )

        print_results(
            "BEFORE RERANKING",
            retrieved,
        )

        print_results(
            "AFTER RERANKING",
            reranked,
        )


if __name__ == "__main__":
    main()