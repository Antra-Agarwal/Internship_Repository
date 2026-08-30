"""
Week 4 - Advanced RAG Application

Reuses Week 3:
- Google Embeddings
- FAISS
- BM25
- Hybrid Retrieval
- Cross Encoder
- Gemini LLM

Adds:
- Query rewriting
- Query expansion
- Multi-query retrieval
- Metadata filtering
- Source citations
- No-answer handling
"""

from dotenv import load_dotenv

# Week 3 components
from week3.src.embeddings.google_embedding_model import (
    GoogleEmbeddingModel,
)

from week3.src.llms import GoogleLLM

from week3.src.vectorstores import FAISSVectorStore

from week3.src.retrievers import VectorStoreRetriever

from week3.src.retrievers.bm25_retriever import (
    BM25Retriever,
)

from week3.src.retrievers.hybrid_retriever import (
    HybridRetriever,
)

from week3.src.rerankers import (
    CrossEncoderReranker,
)

# Week 4 components
from week4.src.query.query_transformer import (
    QueryTransformer,
)

from week4.src.rag.advanced_rag import (
    AdvancedRAG,
)


VECTOR_DB_PATH = "week3/data/vector_db"


def initialize_rag():

    print("Loading embedding model...")

    embedding_model = GoogleEmbeddingModel()

    # -----------------------------------------
    # Load existing Week 3 FAISS database
    # -----------------------------------------

    print("Loading vector database...")

    vector_store = FAISSVectorStore()

    vector_store.load(VECTOR_DB_PATH)

    # -----------------------------------------
    # Dense retrieval
    # -----------------------------------------

    vector_retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    # -----------------------------------------
    # BM25 retrieval
    # -----------------------------------------

    bm25_retriever = BM25Retriever(
        vector_store=vector_store,
    )

    # -----------------------------------------
    # Hybrid retrieval
    # -----------------------------------------

    retriever = HybridRetriever(
        vector_retriever=vector_retriever,
        bm25_retriever=bm25_retriever,
    )

    # -----------------------------------------
    # Cross encoder
    # -----------------------------------------

    reranker = CrossEncoderReranker()

    # -----------------------------------------
    # LLM
    # -----------------------------------------

    llm = GoogleLLM(
        temperature=0.2,
    )

    # -----------------------------------------
    # Query transformer
    # -----------------------------------------

    query_transformer = QueryTransformer(
        llm=GoogleLLM(
            temperature=0.0,
        )
    )

    # -----------------------------------------
    # Advanced RAG
    # -----------------------------------------

    return AdvancedRAG(
        retriever=retriever,
        llm=llm,
        reranker=reranker,
        query_transformer=query_transformer,
        retrieval_k=10,
        final_k=3,
    )


def main():

    load_dotenv()

    print("=" * 60)
    print("WEEK 4 - ADVANCED RAG")
    print("=" * 60)

    rag = initialize_rag()

    print("\nApplication ready.")
    print("Type 'exit' to quit.\n")

    while True:

        question = input("You: ").strip()

        if question.lower() == "exit":
            break

        if not question:
            continue

        response = rag.answer(
            question=question,
        )

        print("\nAssistant:")
        print(response["answer"])

        print("\nSources:")

        if response["sources"]:

            for source in response["sources"]:
                print(f"  - {source}")

        else:
            print("  No sources found.")

        print()


if __name__ == "__main__":
    main()