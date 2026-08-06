"""
Automated evaluation for the Week 3 RAG Agent.
"""

import sys
import time
from pathlib import Path

from dotenv import load_dotenv

# Allow imports from project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app import (
    initialize_agent,
    initialize_tools,
)
from evaluation.test_queries import TEST_QUERIES


OUTPUT_FILE = Path("evaluation/results.md")


def main():

    load_dotenv()

    print("=" * 60)
    print("RUNNING EVALUATION")
    print("=" * 60)

    agent = initialize_agent()
    tool_executor = initialize_tools()

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8",
    ) as report:

        report.write("# Evaluation Results\n\n")

        for index, query in enumerate(
            TEST_QUERIES,
            start=1,
        ):

            print(f"\n[{index}/20] {query}")

            start = time.perf_counter()

            try:

                tool_result = tool_executor.execute(
                    query
                )

                if tool_result is not None:

                    answer = tool_result
                    route = "Tool"

                else:

                    response = agent.invoke(
                        query
                    )

                    answer = response["answer"]

                    route = response["metadata"].get(
                        "route",
                        "Unknown",
                    )

                status = "PASS"

            except Exception as error:

                answer = (
                    f"ERROR: {error}"
                )

                route = "Failed"

                status = "FAIL"

            latency = (
                time.perf_counter()
                - start
            )

            report.write(
                f"## TC-{index:02d}\n\n"
            )

            report.write(
                f"**Query:** {query}\n\n"
            )

            report.write(
                f"**Status:** {status}\n\n"
            )

            report.write(
                f"**Route:** {route}\n\n"
            )

            report.write(
                f"**Latency:** {latency:.3f} sec\n\n"
            )

            report.write(
                "**Response:**\n\n"
            )

            report.write(
                f"{answer}\n\n"
            )

            report.write(
                "---\n\n"
            )

            print(
                f"Status  : {status}"
            )

            print(
                f"Latency : {latency:.3f}s"
            )

    print("\nEvaluation completed.")

    print(
        f"Results saved to {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    main()