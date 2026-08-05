"""
File Reader tool.
"""

from pathlib import Path

from .base_tool import BaseTool


class FileReaderTool(BaseTool):
    """
    Reads the contents of a text file.
    """

    SUPPORTED_EXTENSIONS = {
        ".txt",
        ".md",
        ".py",
        ".json",
        ".csv",
    }

    @property
    def name(self) -> str:
        return "file_reader"

    @property
    def description(self) -> str:
        return (
            "Reads the contents of a text-based file "
            "given its file path."
        )

    def run(
        self,
        input_data: str,
    ) -> str:
        """
        Read a file and return its contents.

        Args:
            input_data:
                Path to the file.

        Returns:
            File contents or an error message.
        """

        try:

            path = Path(input_data).expanduser().resolve()

            if not path.exists():
                return "Error: File does not exist."

            if not path.is_file():
                return "Error: Path is not a file."

            if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                return (
                    f"Error: Unsupported file type '{path.suffix}'."
                )

            return path.read_text(
                encoding="utf-8",
            )

        except Exception as e:
            return f"File Reader Error: {e}"