"""
Manager for loading documents from files or directories.

This class automatically selects the appropriate loader based on
the file extension.
"""

from pathlib import Path
from typing import ClassVar

from langchain_core.documents import Document

from src.exceptions import UnsupportedDocumentTypeError
from src.loaders.docx_loader import DocxLoader
from src.loaders.markdown_loader import MarkdownLoader
from src.loaders.pdf_loader import PDFLoader
from src.loaders.txt_loader import TxtLoader


class DocumentLoaderManager:
    """
    Loads supported documents using the appropriate loader.
    """

    # Mapping of supported file extensions to their loader classes.
    # Shared across all instances of DocumentLoaderManager.
    SUPPORTED_LOADERS: ClassVar[dict[str, type]] = {
        ".pdf": PDFLoader,
        ".docx": DocxLoader,
        ".md": MarkdownLoader,
        ".txt": TxtLoader,
    }

    def _get_loader(self, file_path: Path):
        """
        Return the appropriate loader for a document.

        Args:
            file_path:
                Path to the document.

        Returns:
            Loader instance.

        Raises:
            UnsupportedDocumentTypeError:
                If the document type is not supported.
        """

        suffix = file_path.suffix.lower()

        loader_class = self.SUPPORTED_LOADERS.get(suffix)

        if loader_class is None:
            raise UnsupportedDocumentTypeError(suffix)

        return loader_class()

    def load_file(
        self,
        file_path: str,
    ) -> list[Document]:
        """
        Load a single document.

        Args:
            file_path:
                Path to the document.

        Returns:
            List of LangChain Document objects.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(
                f"File not found: {file_path}"
            )

        if not path.is_file():
            raise ValueError(
                f"{file_path} is not a file."
            )

        loader = self._get_loader(path)

        return loader.load(str(path))

    def load_directory(
        self,
        directory: str,
    ) -> list[Document]:
        """
        Load all supported documents from a directory.

        Unsupported document types are skipped.

        Args:
            directory:
                Path to the directory.

        Returns:
            List of LangChain Document objects.
        """

        directory_path = Path(directory)

        if not directory_path.exists():
            raise FileNotFoundError(
                f"Directory not found: {directory}"
            )

        if not directory_path.is_dir():
            raise NotADirectoryError(
                f"{directory} is not a directory."
            )

        documents: list[Document] = []

        for file_path in sorted(directory_path.iterdir()):

            if not file_path.is_file():
                continue

            try:
                documents.extend(
                    self.load_file(str(file_path))
                )

            except UnsupportedDocumentTypeError:
                continue

        if not documents:
            raise ValueError(
                "No supported documents found in the directory."
            )

        return documents