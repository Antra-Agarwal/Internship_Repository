"""
Test File Reader Tool.
"""

from pathlib import Path

from src.tools import FileReaderTool


def main():

    sample = Path("sample.txt")

    sample.write_text(
        "Hello from the File Reader Tool!\n"
        "This is a sample file.",
        encoding="utf-8",
    )

    tool = FileReaderTool()

    print("=" * 60)
    print("FILE READER TOOL TEST")
    print("=" * 60)

    result = tool.run(str(sample))

    print(result)


if __name__ == "__main__":
    main()