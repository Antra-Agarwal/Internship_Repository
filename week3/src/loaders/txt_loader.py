from pathlib import Path
from typing import List

from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document


class TxtLoader:
    def __init__(self):
        pass

    def load(self, file_path: str) -> List[Document]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"Text file not found: {file_path}")

        try:
            loader = TextLoader(str(path), encoding="utf-8")
            documents = loader.load()
            return documents

        except Exception as e:
            raise RuntimeError(f"Failed to load text file: {file_path}") from e