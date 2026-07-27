"""
Integration test for the FAISS vector store.
"""

from pathlib import Path

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.loaders import DocumentLoaderManager
from src.processing.document_processor import DocumentProcessor
from src.processing.recursive_chunker import RecursiveChunker
from src.vectorstores import FAISSVectorStore


DOCUMENTS_DIR = Path("data/documents")
VECTOR_DB_PATH = "data/vector_db"

QUERY = "What is deadlock?"


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
        RecursiveChunker()
    )

    chunks = processor.process_documents(
        documents
    )

    print(f"Generated {len(chunks)} chunk(s).")

    return chunks


def generate_embeddings(chunks):
    """
    Generate embeddings.
    """

    print("\nGenerating embeddings...")

    embedding_model = GoogleEmbeddingModel()

    embeddings = embedding_model.embed_documents(
        chunks
    )

    print(f"Generated {len(embeddings)} embeddings.")
    print(f"Embedding Dimension : {len(embeddings[0])}")

    return embedding_model, embeddings


def build_vector_store(
    embeddings,
    chunks,
):
    """
    Build the vector store.
    """

    print("\nBuilding vector store...")

    vector_store = FAISSVectorStore()

    vector_store.add(
        embeddings,
        chunks,
    )

    print(f"Indexed Vectors : {len(vector_store)}")

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

        preview = result.document.page_content[:300]

        print(preview)
        print("-" * 60)


def test_search(
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

    return query_embedding


def test_save_load(
    vector_store,
    query_embedding,
):
    """
    Test save/load.
    """

    print("\nSaving vector store...")

    vector_store.save(
        VECTOR_DB_PATH
    )

    print("Vector store saved successfully.")

    print("\nLoading vector store...")

    loaded_store = FAISSVectorStore()

    loaded_store.load(
        VECTOR_DB_PATH
    )

    print("Vector store loaded successfully.")
    print(f"Indexed Vectors : {len(loaded_store)}")

    print("\nVerifying loaded vector store...")

    results = loaded_store.search(
        query_embedding,
        k=3,
    )

    display_results(results)


def main():

    print("=" * 60)
    print("FAISS VECTOR STORE INTEGRATION TEST")
    print("=" * 60)

    documents = load_documents()

    chunks = process_documents(
        documents
    )

    embedding_model, embeddings = generate_embeddings(
        chunks
    )

    vector_store = build_vector_store(
        embeddings,
        chunks,
    )

    query_embedding = test_search(
        vector_store,
        embedding_model,
    )

    test_save_load(
        vector_store,
        query_embedding,
    )

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()