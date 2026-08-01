"""
Integration test for the complete RAG pipeline.
"""

from dotenv import load_dotenv

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.llms import GoogleLLM
from src.rag import RAGPipeline
from src.rerankers import CrossEncoderReranker
from src.retrievers import VectorStoreRetriever
from src.vectorstores import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"


def test_rag():

    load_dotenv()

    print("\nLoading embedding model...")

    embedding_model = GoogleEmbeddingModel()

    print("Loading vector store...")

    vector_store = FAISSVectorStore()

    vector_store.load(
        VECTOR_DB_PATH
    )

    print(f"Indexed Vectors : {len(vector_store)}")

    print("\nInitializing Retriever...")

    retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    print("Initializing Cross-Encoder Reranker...")

    reranker = CrossEncoderReranker()

    print("Initializing LLM...")

    llm = GoogleLLM()

    print("Initializing RAG Pipeline...")

    rag = RAGPipeline(
        retriever=retriever,
        reranker=reranker,
        llm=llm,
    )

    while True:

        question = input(
            "\nEnter a question (or 'exit'): "
        ).strip()

        if question.lower() == "exit":
            break

        if not question:
            continue

        print("\nQuestion")
        print("=" * 60)
        print(question)

        answer = rag.answer(
            question=question,
            retrieval_k=10,
            k=3,
        )

        print("\nAnswer")
        print("=" * 60)
        print(answer)


def main():

    print("=" * 60)
    print("RAG PIPELINE INTEGRATION TEST")
    print("=" * 60)

    test_rag()

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()