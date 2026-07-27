from pathlib import Path

from tests.test_utils import (
    create_chunkers,
    load_documents,
    print_results,
)


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DOCUMENTS_DIR = PROJECT_ROOT / "data" / "documents"


# ==========================================================
# Main
# ==========================================================

def main():
    print("\nLoading documents...\n")

    documents = load_documents(str(DOCUMENTS_DIR))

    print(f"Loaded {len(documents)} document(s).\n")

    for name, chunker in create_chunkers():

        print("=" * 80)
        print(f"Running {name}...")
        print("=" * 80)

        try:
            chunks = chunker.split_documents(documents)

            print_results(
                name=name,
                chunks=chunks,
            )

        except Exception as error:
            print(f"{name} failed.")
            print(f"Reason: {error}")
            print()

    print("=" * 80)
    print("Chunker comparison completed.")
    print("=" * 80)


if __name__ == "__main__":
    main()