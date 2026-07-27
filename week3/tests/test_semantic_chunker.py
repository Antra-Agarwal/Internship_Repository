from langchain_core.documents import Document

from src.embeddings.google_embedding_model import GoogleEmbeddingModel
from src.processing.custom_semantic_chunker import CustomSemanticChunker
from src.processing.semantic_similarity import AdjacentSimilarityStrategy


def main():

    document = Document(
        page_content="""
        LangChain is a framework for developing LLM applications.

        It provides components such as prompts, chains and agents.

        Embeddings convert text into numerical vectors.

        Vector databases store embeddings for efficient retrieval.

        Pizza is a popular Italian food.

        Pasta is another famous Italian dish.

        Machine learning enables computers to learn from data.

        Deep learning is a subset of machine learning.
        """,
        metadata={
            "source": "sample.txt"
        }
    )

    embedding_model = GoogleEmbeddingModel()

    similarity_strategy = AdjacentSimilarityStrategy()

    chunker = CustomSemanticChunker(
        embedding_model=embedding_model,
        similarity_strategy=similarity_strategy,
        chunk_size=300,
        similarity_threshold=0.80,
    )

    chunks = chunker.split_documents([document])

    print("=" * 60)
    print("SEMANTIC CHUNKING RESULTS")
    print("=" * 60)

    print(f"\nTotal Chunks: {len(chunks)}\n")

    for i, chunk in enumerate(chunks, start=1):

        print(f"Chunk {i}")
        print("-" * 40)

        print(chunk.page_content)

        print("\nMetadata:")

        for key, value in chunk.metadata.items():
            print(f"{key}: {value}")

        print("\nLength:", len(chunk.page_content))

        print("\n" + "=" * 60)


if __name__ == "__main__":
    main()