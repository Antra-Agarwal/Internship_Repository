from src.embeddings.google_embedding_model import GoogleEmbeddingModel


def main():

    embedding_model = GoogleEmbeddingModel()

    texts = [
        "Python is a programming language.",
        "Machine learning enables computers to learn from data.",
        "LangChain simplifies LLM application development."
    ]

    print("=" * 60)
    print("DOCUMENT EMBEDDINGS")
    print("=" * 60)

    document_embeddings = embedding_model.embed_documents(texts)

    print(f"Texts                : {len(texts)}")
    print(f"Embeddings Generated : {len(document_embeddings)}")
    print(f"Embedding Dimension  : {len(document_embeddings[0])}")

    print("\nFirst 10 values of first embedding:")

    print(document_embeddings[0][:10])

    print()

    print("=" * 60)
    print("QUERY EMBEDDING")
    print("=" * 60)

    query = "What is Python?"

    query_embedding = embedding_model.embed_query(query)

    print(f"Embedding Dimension : {len(query_embedding)}")

    print("\nFirst 10 values:")

    print(query_embedding[:10])


if __name__ == "__main__":
    main()