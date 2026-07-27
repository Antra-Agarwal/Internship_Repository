from langchain_core.documents import Document

from src.embeddings.google_embedding_model import GoogleEmbeddingModel


def main():
    """
    Test the Google embedding model.
    """

    # Sample documents
    documents = [
        Document(
            page_content="Database normalization reduces data redundancy."
        ),
        Document(
            page_content="Indexes improve query performance."
        ),
        Document(
            page_content="Transactions ensure ACID properties."
        ),
    ]

    # Initialize embedding model
    embedding_model = GoogleEmbeddingModel()

    # Generate embeddings
    document_embeddings = embedding_model.embed_documents(documents)
    query_embedding = embedding_model.embed_query(
        "What is database normalization?"
    )

    print("=" * 60)
    print("DOCUMENT EMBEDDINGS")
    print("=" * 60)

    print(f"Documents Processed      : {len(documents)}")
    print(f"Embeddings Generated    : {len(document_embeddings)}")
    print(f"Embedding Dimension     : {len(document_embeddings[0])}")
    print(f"Embedding Data Type     : {type(document_embeddings[0])}")

    print("\nFirst Document:")
    print(documents[0].page_content)

    print("\nFirst 10 Embedding Values:")
    print(document_embeddings[0][:10])

    print("\n" + "=" * 60)
    print("QUERY EMBEDDING")
    print("=" * 60)

    print("Query:")
    print("What is database normalization?")

    print(f"\nEmbedding Dimension     : {len(query_embedding)}")
    print(f"Embedding Data Type     : {type(query_embedding)}")

    print("\nFirst 10 Embedding Values:")
    print(query_embedding[:10])

    print("\n" + "=" * 60)
    print("TEST PASSED")
    print("=" * 60)
    print("✓ Document embeddings generated successfully.")
    print("✓ Query embedding generated successfully.")
    print("✓ Google Embedding Model is working correctly.")


if __name__ == "__main__":
    main()