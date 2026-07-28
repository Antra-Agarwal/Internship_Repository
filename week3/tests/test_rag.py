"""
Integration test for the complete RAG pipeline.
"""

from pathlib import Path

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.llms import GoogleLLM
from src.loaders import DocumentLoaderManager
from src.processing.document_processor import DocumentProcessor
from src.processing.recursive_chunker import RecursiveChunker
from src.rag import RAGPipeline
from src.retrievers import VectorStoreRetriever
from src.vectorstores import FAISSVectorStore


DOCUMENTS_DIR = Path("data/documents")

QUESTION = "What is a Database?"


def load_documents():

    print("\nLoading documents...")

    manager = DocumentLoaderManager()

    documents = manager.load_directory(
        str(DOCUMENTS_DIR)
    )

    print(f"Loaded {len(documents)} document(s).")

    return documents


def process_documents(documents):

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

    return embedding_model, embeddings


def build_vector_store(
    embeddings,
    chunks,
):

    print("\nBuilding vector store...")

    vector_store = FAISSVectorStore()

    vector_store.add(
        embeddings,
        chunks,
    )

    print(f"Indexed Vectors : {len(vector_store)}")

    return vector_store


def test_rag(
    embedding_model,
    vector_store,
):

    print("\nInitializing Retriever...")

    retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    print("Initializing LLM...")

    llm = GoogleLLM()

    print("Initializing RAG Pipeline...")

    rag = RAGPipeline(
        retriever=retriever,
        llm=llm,
    )

    print("\nQuestion")
    print("=" * 60)
    print(QUESTION)

    answer = rag.answer(
        QUESTION,
        k=3,
    )

    print("\nAnswer")
    print("=" * 60)
    print(answer)


def main():

    print("=" * 60)
    print("RAG PIPELINE INTEGRATION TEST")
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

    test_rag(
        embedding_model,
        vector_store,
    )

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()