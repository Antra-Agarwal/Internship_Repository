from pathlib import Path
from typing import List

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> List[Document]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {file_path}")

        try:
            loader = PyPDFLoader(str(path))
            documents = loader.load()
            return documents

        except Exception as e:
            raise RuntimeError(f"Failed to load PDF: {file_path}") from e