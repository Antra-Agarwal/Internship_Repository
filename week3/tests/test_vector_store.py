"""
Integration test for the FAISS vector store.
"""

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.vectorstores import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"

QUERY = "What is a Database?"


def load_vector_store():
    """
    Load an existing vector database.
    """

    print("\nLoading vector database...")

    vector_store = FAISSVectorStore()

    vector_store.load(
        VECTOR_DB_PATH
    )

    print("Vector database loaded successfully.")
    print(f"Indexed vectors : {len(vector_store)}")

    return vector_store


def display_results(results):
    """
    Display search results.
    """

    print("\nTop Search Results")
    print("=" * 60)

    for i, result in enumerate(
        results,
        start=1,
    ):
        print(f"\nResult {i}")
        print(f"Distance : {result.score:.4f}")

        metadata = result.document.metadata

        print(f"Source   : {metadata.get('source')}")
        print(f"Page     : {metadata.get('page')}")

        preview = (
            result.document.page_content[:300]
            .replace("\n", " ")
            .strip()
        )

        print(preview)
        print("-" * 60)


def test_similarity_search(
    vector_store,
    embedding_model,
):
    """
    Test similarity search.
    """

    print("\nTesting similarity search...")

    query_embedding = embedding_model.embed_query(
        QUERY
    )

    results = vector_store.search(
        query_embedding,
        k=3,
    )

    display_results(results)

    return query_embedding, results


def test_reload(
    query_embedding,
):
    """
    Verify that the saved vector database
    can be loaded correctly.
    """

    print("\nReloading vector database...")

    loaded_store = FAISSVectorStore()

    loaded_store.load(
        VECTOR_DB_PATH
    )

    print("Vector database loaded successfully.")
    print(f"Indexed vectors : {len(loaded_store)}")

    print("\nVerifying loaded vector database...")

    results = loaded_store.search(
        query_embedding,
        k=3,
    )

    display_results(results)


def main():

    load_dotenv()

    print("=" * 60)
    print("FAISS VECTOR STORE INTEGRATION TEST")
    print("=" * 60)

    embedding_model = GoogleEmbeddingModel()

    vector_store = load_vector_store()

    query_embedding, _ = test_similarity_search(
        vector_store,
        embedding_model,
    )

    test_reload(
        query_embedding,
    )

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()