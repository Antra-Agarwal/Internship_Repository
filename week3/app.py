"""
Production AI Assistant.

Features:
- Tool Routing
- Calculator Tool
- File Reader Tool
- Hybrid RAG Agent
"""

from dotenv import load_dotenv
from src.utils.logger import get_logger

from src.agents import RAGAgent
from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.llms import GoogleLLM
from src.memory import ConversationMemory
from src.rerankers import CrossEncoderReranker
from src.retrievers import VectorStoreRetriever
from src.retrievers.bm25_retriever import BM25Retriever
from src.retrievers.hybrid_retriever import HybridRetriever
from src.tools import (
    CalculatorTool,
    FileReaderTool,
    ToolRegistry,
)
from src.tools.tool_executor import ToolExecutor
from src.vectorstores import FAISSVectorStore


VECTOR_DB_PATH = "data/vector_db"


def initialize_agent() -> RAGAgent:

    embedding_model = GoogleEmbeddingModel()

    vector_store = FAISSVectorStore()
    vector_store.load(VECTOR_DB_PATH)

    # Dense Retriever
    vector_retriever = VectorStoreRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    # Sparse Retriever
    bm25_retriever = BM25Retriever(
        vector_store=vector_store,
    )

    # Hybrid Retriever (RRF)
    retriever = HybridRetriever(
        vector_retriever=vector_retriever,
        bm25_retriever=bm25_retriever,
    )

    reranker = CrossEncoderReranker()

    router_llm = GoogleLLM(
        temperature=0.0,
    )

    generator_llm = GoogleLLM(
        temperature=0.2,
    )

    return RAGAgent(
        retriever=retriever,
        router_llm=router_llm,
        generator_llm=generator_llm,
        reranker=reranker,
        retrieval_k=10,
        final_k=3,
        rerank_threshold=0.0,
    )


def initialize_tools() -> ToolExecutor:

    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )

    registry.register(
        FileReaderTool()
    )

    return ToolExecutor(registry)


def main():

    load_dotenv()
    logger = get_logger("App")


    print("=" * 60)
    print("RAG AI ASSISTANT")
    print("=" * 60)

    logger.info("Loading RAG agent...")

    agent = initialize_agent()

    logger.info("Loading tools...")

    tool_executor = initialize_tools()

    # Initialize conversation memory
    memory = ConversationMemory(
        max_turns=5,
    )

    logger.info("Application ready.")
    print()

    while True:

        question = input("You : ").strip()
        logger.info(
            f"User Question: {question}"
        )

        if question.lower() == "exit":
            break

        if not question:
            continue

        # Store user message
        memory.add_user_message(question)

        tool_result = tool_executor.execute(question)

        if tool_result is not None:

            print("\nAssistant:")
            print(tool_result)
            logger.info(
                "Response generated using ToolExecutor."
            )

            # Store assistant response
            memory.add_assistant_message(
                tool_result
            )

            continue

        response = agent.invoke(question)
        logger.info(
            "Response generated using RAG agent."
        )

        print("\nAssistant:")
        print(response["answer"])

        # Store assistant response
        memory.add_assistant_message(
            response["answer"]
        )


if __name__ == "__main__":
    main()