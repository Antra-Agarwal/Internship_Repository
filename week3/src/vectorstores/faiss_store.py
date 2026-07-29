"""
FAISS vector store implementation.
"""

from pathlib import Path
import pickle

import faiss
import numpy as np
from langchain_core.documents import Document

from src.vectorstores.base import (
    BaseVectorStore,
    SearchResult,
)


class FAISSVectorStore(BaseVectorStore):
    """
    FAISS-based implementation of a vector store.

    The FAISS index is created automatically when the first batch of
    embeddings is added.
    """

    def __init__(self):
        """
        Initialize an empty vector store.
        """
        self.dimension: int | None = None
        self._index: faiss.Index | None = None
        self._documents: list[Document] = []

    def _initialize_index(
        self,
        dimension: int,
    ) -> None:
        """
        Create the FAISS index.

        Args:
            dimension: Embedding dimension.
        """
        self.dimension = dimension
        self._index = faiss.IndexFlatL2(dimension)

    def add(
        self,
        embeddings: list[list[float]],
        documents: list[Document],
    ) -> None:
        """
        Add embeddings and documents to the vector store.

        Args:
            embeddings: List of embedding vectors.
            documents: Corresponding LangChain documents.
        """

        if not embeddings:
            raise ValueError("Embeddings cannot be empty.")

        if len(embeddings) != len(documents):
            raise ValueError(
                "Embeddings and documents must have the same length."
            )

        embedding_dimension = len(embeddings[0])

        # Initialize the FAISS index on the first insertion.
        if self._index is None:
            self._initialize_index(embedding_dimension)

        # Validate embedding dimensions.
        for embedding in embeddings:
            if len(embedding) != self.dimension:
                raise ValueError(
                    f"Expected embedding dimension "
                    f"{self.dimension}, "
                    f"received {len(embedding)}."
                )

        vectors = np.asarray(
            embeddings,
            dtype=np.float32,
        )

        self._index.add(vectors)
        self._documents.extend(documents)

    def search(
        self,
        query_embedding: list[float],
        k: int = 5,
    ) -> list[SearchResult]:
        """
        Search for the most similar documents.

        Args:
            query_embedding: Query embedding vector.
            k: Number of nearest neighbours to retrieve.

        Returns:
            List of SearchResult objects sorted by increasing L2 distance.
            A smaller score indicates a more similar document.
        """

        if self._index is None:
            return []

        if k <= 0:
            raise ValueError(
                "k must be greater than zero."
            )

        if len(query_embedding) != self.dimension:
            raise ValueError(
                f"Expected embedding dimension "
                f"{self.dimension}, "
                f"received {len(query_embedding)}."
            )

        # Do not request more neighbours than exist.
        k = min(k, len(self._documents))

        query_vector = np.asarray(
            [query_embedding],
            dtype=np.float32,
        )

        distances, indices = self._index.search(
            query_vector,
            k,
        )

        results: list[SearchResult] = []

        for distance, index in zip(
            distances[0],
            indices[0],
        ):
            if index == -1:
                continue

            results.append(
                SearchResult(
                    document=self._documents[index],
                    score=float(distance),
                )
            )

        return results

    def save(
        self,
        path: str,
    ) -> None:
        """
        Save the vector store.

        Args:
            path: Directory where the vector store will be saved.
        """

        if self._index is None:
            raise RuntimeError(
                "Cannot save an empty vector store."
            )

        save_dir = Path(path)
        save_dir.mkdir(
            parents=True,
            exist_ok=True,
        )

        faiss.write_index(
            self._index,
            str(save_dir / "index.faiss"),
        )

        with open(
            save_dir / "documents.pkl",
            "wb",
        ) as file:
            pickle.dump(
                self._documents,
                file,
            )

    def load(
        self,
        path: str,
    ) -> None:
        """
        Load a previously saved vector store.

        Args:
            path: Directory containing the FAISS index and documents.
        """

        load_dir = Path(path)

        index_path = load_dir / "index.faiss"
        documents_path = load_dir / "documents.pkl"

        if not index_path.exists():
            raise FileNotFoundError(
                f"{index_path} does not exist."
            )

        if not documents_path.exists():
            raise FileNotFoundError(
                f"{documents_path} does not exist."
            )

        self._index = faiss.read_index(
            str(index_path)
        )

        self.dimension = self._index.d

        with open(
            documents_path,
            "rb",
        ) as file:
            self._documents = pickle.load(file)

    def __len__(self) -> int:
        """
        Return the number of indexed vectors.
        """

        if self._index is None:
            return 0

        return self._index.ntotal