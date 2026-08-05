"""
Calculator tool.
"""

import ast
import operator

from .base_tool import BaseTool


class CalculatorTool(BaseTool):
    """
    Safely evaluate mathematical expressions.
    """

    _OPERATORS = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg,
    }

    @property
    def name(self) -> str:
        return "calculator"

    @property
    def description(self) -> str:
        return (
            "Evaluates mathematical expressions "
            "containing +, -, *, /, %, ** and parentheses."
        )

    def run(
        self,
        input_data: str,
    ) -> str:

        try:

            tree = ast.parse(
                input_data,
                mode="eval",
            )

            result = self._evaluate(tree.body)

            return str(result)

        except Exception as e:
            return f"Calculation Error: {e}"

    def _evaluate(
        self,
        node,
    ):

        if isinstance(node, ast.Constant):
            return node.value

        if isinstance(node, ast.Num):
            return node.n

        if isinstance(node, ast.BinOp):

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            return self._OPERATORS[type(node.op)](
                left,
                right,
            )

        if isinstance(node, ast.UnaryOp):

            operand = self._evaluate(node.operand)

            return self._OPERATORS[type(node.op)](
                operand,
            )

        raise ValueError("Unsupported expression.")