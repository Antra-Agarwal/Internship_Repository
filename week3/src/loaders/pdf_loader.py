from pathlib import Path
from typing import List, Optional

from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document


class PDFLoader:
    def __init__(self):
        pass

    def load(
        self,
        file_path: str,
        max_pages: Optional[int] = None,
    ) -> List[Document]:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"PDF not found: {file_path}")

        try:
            loader = PyPDFLoader(str(path))

            if max_pages is None:
                return loader.load()

            documents = []

            for i, document in enumerate(loader.lazy_load()):
                if i >= max_pages:
                    break
                documents.append(document)

            return documents

        except Exception as e:
            raise RuntimeError(f"Failed to load PDF: {file_path}") from e