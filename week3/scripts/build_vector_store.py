from pathlib import Path

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.loaders import DocumentLoaderManager
from src.processing.document_processor import DocumentProcessor
from src.processing.recursive_chunker import RecursiveChunker
from src.vectorstores import FAISSVectorStore


DOCUMENTS_DIR = Path("data/documents")
VECTOR_DB_PATH = "data/vector_db"


def main():

    load_dotenv()

    print("=" * 70)
    print("BUILDING VECTOR DATABASE")
    print("=" * 70)

    # Load documents
    print("\nLoading documents...")

    manager = DocumentLoaderManager()

    documents = manager.load_directory(
        str(DOCUMENTS_DIR)
    )

    print(f"Loaded {len(documents)} document(s).")

    # Chunk documents
    print("\nProcessing documents...")

    processor = DocumentProcessor(
        RecursiveChunker()
    )

    chunks = processor.process_documents(
        documents
    )

    print(f"Generated {len(chunks)} chunk(s).")

    # Generate embeddings
    print("\nGenerating embeddings...")

    embedding_model = GoogleEmbeddingModel()

    texts = [
        chunk.page_content
        for chunk in chunks
    ]

    embeddings = embedding_model.embed_documents(
        texts
    )

    print(f"Generated {len(embeddings)} embeddings.")

    # Build vector store
    print("\nBuilding vector store...")

    vector_store = FAISSVectorStore()

    vector_store.add(
        embeddings,
        chunks,
    )

    print(f"Indexed vectors : {len(vector_store)}")

    # Save vector store
    print("\nSaving vector database...")

    vector_store.save(
        VECTOR_DB_PATH
    )

    print(f"Vector database saved to '{VECTOR_DB_PATH}'.")

    print("\n" + "=" * 70)
    print("VECTOR DATABASE BUILT SUCCESSFULLY")
    print("=" * 70)


if __name__ == "__main__":
    main()