from typing import List

import spacy
from langchain_core.documents import Document

from src.constants import CUSTOM_SEMANTIC_CHUNKER
from src.embeddings.base_embedding import BaseEmbedding
from src.processing.base_semantic_chunker import BaseSemanticChunker
from src.processing.semantic_similarity import SimilarityStrategy


# Load the spaCy model once when the module is imported.
try:
    _NLP = spacy.load("en_core_web_sm")
except OSError as exc:
    raise RuntimeError(
        "spaCy model 'en_core_web_sm' is not installed.\n"
        "Install it using:\n"
        "python -m spacy download en_core_web_sm"
    ) from exc


class CustomSemanticChunker(BaseSemanticChunker):
    """
    Custom semantic chunker that groups semantically similar
    sentences using sentence embeddings and a configurable
    similarity strategy.
    """

    def __init__(
        self,
        embedding_model: BaseEmbedding,
        similarity_strategy: SimilarityStrategy,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        similarity_threshold: float = 0.80,
    ):
        """
        Initialize the semantic chunker.

        Args:
            embedding_model: Embedding model used to generate sentence embeddings.
            similarity_strategy: Strategy used to compute semantic similarity.
            chunk_size: Maximum chunk size (in characters).
            chunk_overlap: Reserved for future sentence-level overlap.
            similarity_threshold: Minimum similarity required for adjacent
                sentences to remain in the same chunk.
        """
        super().__init__(
            embedding_model=embedding_model,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        self._similarity_strategy = similarity_strategy
        self._similarity_threshold = similarity_threshold

        # Reuse the globally loaded spaCy model.
        self._nlp = _NLP

    def split_documents(
        self,
        documents: List[Document],
    ) -> List[Document]:
        """
        Split documents into semantic chunks.
        """

        chunked_documents = []

        for document in documents:

            sentences = self._extract_sentences(
                document.page_content
            )

            if not sentences:
                continue

            similarities = self._compute_similarities(
                sentences
            )

            semantic_chunks = self._build_semantic_chunks(
                sentences,
                similarities,
            )

            chunked_documents.extend(
                self._build_chunk_documents(
                    semantic_chunks,
                    document.metadata,
                )
            )

        return chunked_documents

    def _extract_sentences(
        self,
        text: str,
    ) -> List[str]:
        """
        Extract sentences from text using spaCy.
        """

        doc = self._nlp(text)

        return [
            sentence.text.strip()
            for sentence in doc.sents
            if sentence.text.strip()
        ]

    def _compute_similarities(
        self,
        sentences: List[str],
    ) -> List[float]:
        """
        Generate sentence embeddings and compute similarity
        scores between adjacent sentences.
        """

        if len(sentences) < 2:
            return []

        embeddings = self.embedding_model.embed_documents(
            sentences
        )

        return self._similarity_strategy.compute_similarities(
            embeddings
        )

    def _build_semantic_chunks(
        self,
        sentences: List[str],
        similarities: List[float],
    ) -> List[List[str]]:
        """
        Group sentences into semantic chunks based on
        semantic similarity and maximum chunk size.
        """

        if len(sentences) == 1:
            return [sentences]

        chunks: List[List[str]] = []

        current_chunk = [sentences[0]]
        current_size = len(sentences[0])

        for index, similarity in enumerate(similarities):

            next_sentence = sentences[index + 1]

            exceeds_chunk_size = (
                current_size + len(next_sentence)
                > self.chunk_size
            )

            should_split = (
                similarity < self._similarity_threshold
                or exceeds_chunk_size
            )

            if should_split:

                chunks.append(current_chunk)

                current_chunk = [next_sentence]
                current_size = len(next_sentence)

            else:

                current_chunk.append(next_sentence)
                current_size += len(next_sentence)

        if current_chunk:
            chunks.append(current_chunk)

        return chunks

    def _build_chunk_documents(
        self,
        chunks: List[List[str]],
        metadata: dict,
    ) -> List[Document]:
        """
        Convert semantic chunks into LangChain Document objects.
        """

        documents = []

        for index, chunk in enumerate(chunks):

            chunk_metadata = metadata.copy()

            chunk_metadata["chunk_index"] = index
            chunk_metadata["chunking_strategy"] = CUSTOM_SEMANTIC_CHUNKER
            chunk_metadata["sentence_count"] = len(chunk)

            documents.append(
                Document(
                    page_content=" ".join(chunk),
                    metadata=chunk_metadata,
                )
            )

        return documents