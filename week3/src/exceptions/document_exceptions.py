"""
Custom exceptions used by the document loading system.
"""


class UnsupportedDocumentTypeError(Exception):
    """
    Raised when no loader exists for a document type.
    """

    def __init__(self, extension: str):
        super().__init__(
            f"Unsupported document type: '{extension}'"
        )