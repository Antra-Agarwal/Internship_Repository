from week3.src.llms import GoogleLLM


class QueryTransformer:

    def __init__(self, llm=None):
        self.llm = llm or GoogleLLM(temperature=0.0)

    def rewrite(self, query: str) -> str:

        prompt = f"""
Rewrite the following user question into a clear,
specific search query.

Do not answer the question.
Return only the rewritten query.

Question:
{query}
"""

        return self.llm.generate(prompt).strip()

    def expand(self, query: str) -> list[str]:

        prompt = f"""
Generate 3 alternative search queries for the
following user question.

The alternatives should use different wording
while preserving the original meaning.

Return exactly one query per line.
Do not number the queries.

Question:
{query}
"""

        response = self.llm.generate(prompt)

        queries = [
            line.strip()
            for line in response.splitlines()
            if line.strip()
        ]

        return queries[:3]

    def multi_query(self, query: str) -> list[str]:

        rewritten = self.rewrite(query)

        expanded = self.expand(rewritten)

        queries = [query, rewritten] + expanded

        # Remove duplicates
        return list(dict.fromkeys(queries))