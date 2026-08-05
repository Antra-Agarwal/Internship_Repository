"""
Test Tool Executor.
"""

from src.tools import (
    CalculatorTool,
    FileReaderTool,
    ToolRegistry,
)
from src.tools.tool_executor import ToolExecutor


def main():

    registry = ToolRegistry()

    registry.register(
        CalculatorTool()
    )

    registry.register(
        FileReaderTool()
    )

    executor = ToolExecutor(
        registry
    )

    while True:

        query = input(
            "\nQuery (exit): "
        ).strip()

        if query == "exit":
            break

        result = executor.execute(query)

        if result is None:

            print("No tool selected.")

        else:

            print(result)


if __name__ == "__main__":
    main()