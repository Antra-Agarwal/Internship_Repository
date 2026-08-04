"""
Integration test for the LangGraph RAG Agent.
"""

from dotenv import load_dotenv

from src.agents import RAGAgent
from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.llms import GoogleLLM
from src.rerankers import CrossEncoderReranker
from src.retrievers import VectorStoreRetriever
from src.vectorstores import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"


def test_langgraph():

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

    print("Initializing LangGraph Agent...")

    agent = RAGAgent(
        retriever=retriever,
        llm=llm,
        reranker=reranker,
        retrieval_k=10,
        final_k=3,
    )

    while True:

        question = input(
            "\nEnter a question (or 'exit'): "
        ).strip()

        if question.lower() == "exit":
            break

        if not question:
            continue

        response = agent.invoke(question)

        print("\nQuestion")
        print("=" * 60)
        print(response["question"])

        print("\nAnswer")
        print("=" * 60)
        print(response["answer"])

        print("\nRetrieved Documents")
        print("=" * 60)

        for index, result in enumerate(
            response["results"],
            start=1,
        ):
            print(f"\nDocument {index}")
            print(f"Score : {result.score:.4f}")

            source = result.document.metadata.get(
                "source",
                "Unknown",
            )

            print(f"Source : {source}")

            preview = (
                result.document.page_content[:200]
                .replace("\n", " ")
                .strip()
            )

            print(f"Preview : {preview}...")

        print("\nMetadata")
        print("=" * 60)
        print(response["metadata"])


def main():

    print("=" * 60)
    print("LANGGRAPH AGENT INTEGRATION TEST")
    print("=" * 60)

    test_langgraph()

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()