from pathlib import Path
from typing import List

from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.documents import Document


class DocxLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> List[Document]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"DOCX file not found: {file_path}")

        try:
            loader = Docx2txtLoader(str(path))
            documents = loader.load()
            return documents

        except Exception as e:
            raise RuntimeError(f"Failed to load DOCX file: {file_path}") from e