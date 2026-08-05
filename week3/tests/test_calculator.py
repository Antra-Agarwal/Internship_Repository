"""
Test Calculator Tool.
"""

from src.tools import CalculatorTool


def main():

    tool = CalculatorTool()

    expressions = [
        "2+2",
        "15*8",
        "100/5",
        "(5+7)*3",
        "2**10",
        "50%6",
        "-15+20",
    ]

    print("=" * 60)
    print("CALCULATOR TOOL TEST")
    print("=" * 60)

    for expr in expressions:

        result = tool.run(expr)

        print(f"{expr:<20} -> {result}")


if __name__ == "__main__":
    main()