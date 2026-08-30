"""
Week 4 - Advanced RAG Application

Reuses Week 3 components:
- Google Embeddings
- FAISS Vector Store
- BM25
- Hybrid Retrieval
- Cross-Encoder Reranking
- Gemini LLM

Adds Week 4 capabilities:
- Query rewriting
- Query expansion
- Multi-query retrieval
- Metadata filtering
- Source citations
- No-answer handling
"""

from dotenv import load_dotenv

# ============================================================
# Week 3 Components
# ============================================================

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


# ============================================================
# Week 4 Components
# ============================================================

from week4.src.query.query_transformer import (
    QueryTransformer,
)

from week4.src.rag.advanced_rag import (
    AdvancedRAG,
)


# ============================================================
# Configuration
# ============================================================

VECTOR_DB_PATH = "week3/data/vector_db"


# ============================================================
# Metadata Filter
# ============================================================

def get_metadata_filter():
    """
    Ask the user whether they want to restrict the
    search to a particular document.
    """

    print("\nMetadata Filter")
    print("-" * 40)

    print("1. Search all documents")
    print("2. Search Introduction to Database.pdf")

    choice = input("Select option [1]: ").strip()

    if choice == "2":

        return {
            "source": (
                "data\\documents\\Introduction to Database.pdf"
            )
        }

    return None


# ============================================================
# Initialize Advanced RAG
# ============================================================

def initialize_rag():

    print("Loading embedding model...")

    embedding_model = GoogleEmbeddingModel()

    # --------------------------------------------------------
    # Load existing Week 3 FAISS database
    # --------------------------------------------------------

    print("Loading vector database...")

    vector_store = FAISSVectorStore()

    vector_store.load(VECTOR_DB_PATH)

    # --------------------------------------------------------
    # Dense Retriever
    # --------------------------------------------------------

    vector_retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    # --------------------------------------------------------
    # Sparse Retriever
    # --------------------------------------------------------

    bm25_retriever = BM25Retriever(
        vector_store=vector_store,
    )

    # --------------------------------------------------------
    # Hybrid Retriever
    # --------------------------------------------------------

    retriever = HybridRetriever(
        vector_retriever=vector_retriever,
        bm25_retriever=bm25_retriever,
    )

    # --------------------------------------------------------
    # Cross Encoder Reranker
    # --------------------------------------------------------

    print("Loading reranker...")

    reranker = CrossEncoderReranker()

    # --------------------------------------------------------
    # Generator LLM
    # --------------------------------------------------------

    llm = GoogleLLM(
        temperature=0.2,
    )

    # --------------------------------------------------------
    # Query Transformer
    # --------------------------------------------------------

    query_llm = GoogleLLM(
        temperature=0.0,
    )

    query_transformer = QueryTransformer(
        llm=query_llm,
    )

    # --------------------------------------------------------
    # Advanced RAG
    # --------------------------------------------------------

    return AdvancedRAG(
        retriever=retriever,
        llm=llm,
        reranker=reranker,
        query_transformer=query_transformer,
        retrieval_k=10,
        final_k=3,
    )


# ============================================================
# Main Application
# ============================================================

def main():

    load_dotenv()

    print("=" * 60)
    print("WEEK 4 - ADVANCED RAG")
    print("=" * 60)

    print()

    # --------------------------------------------------------
    # Initialize RAG
    # --------------------------------------------------------

    rag = initialize_rag()

    print()
    print("Application ready.")
    print("Type 'exit' to quit.")

    # --------------------------------------------------------
    # Conversation loop
    # --------------------------------------------------------

    while True:

        print()

        question = input("You: ").strip()

        # ----------------------------------------------------
        # Exit
        # ----------------------------------------------------

        if question.lower() == "exit":
            print("\nGoodbye!")
            break

        # ----------------------------------------------------
        # Empty question
        # ----------------------------------------------------

        if not question:

            print(
                "Please enter a question."
            )

            continue

        # ----------------------------------------------------
        # Metadata filtering
        # ----------------------------------------------------

        metadata_filter = get_metadata_filter()

        # ----------------------------------------------------
        # Advanced RAG
        # ----------------------------------------------------

        try:

            response = rag.answer(
                question=question,
                metadata_filter=metadata_filter,
            )

        except Exception as error:

            print("\nError while processing request:")
            print(error)

            continue

        # ----------------------------------------------------
        # Display answer
        # ----------------------------------------------------

        print("\nAssistant:")
        print(response["answer"])

        # ----------------------------------------------------
        # Display sources
        # ----------------------------------------------------

        print("\nSources:")

        sources = response.get("sources", [])

        if sources:

            for source in sources:
                print(f"  - {source}")

        else:

            print("  No sources found.")


# ============================================================
# Entry Point
# ============================================================

if __name__ == "__main__":
    main()