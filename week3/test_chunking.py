from src.loaders.pdf_loader import PDFLoader
from src.processing.chunking import DocumentChunker
from src.processing.document_processor import DocumentProcessor


def main():
    # Load the PDF
    pdf_loader = PDFLoader()
    documents = pdf_loader.load(
        "data/documents/Introduction to Database.pdf",
        max_pages=None
    )

    # Initialize processing pipeline
    chunker = DocumentChunker()
    processor = DocumentProcessor(chunker)

    # Process documents into chunks
    chunks = processor.process_documents(documents)

    # Display summary
    print(f"Pages loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")

    # Display sample chunk
    print("\nFirst Chunk Preview:")
    print("-" * 50)
    print(chunks[0].page_content[:300])

    # Display metadata
    print("\nFirst Chunk Metadata:")
    print("-" * 50)
    print(chunks[0].metadata)


if __name__ == "__main__":
    main()