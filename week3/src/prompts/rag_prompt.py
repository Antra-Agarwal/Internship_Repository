from langchain_core.prompts import PromptTemplate


RAG_PROMPT = PromptTemplate.from_template(
    """
You are a helpful AI assistant.

Answer the question ONLY using the provided context.

If the answer cannot be found in the context,
respond with:

"I don't know based on the provided context."

Context:
{context}

Question:
{question}

Answer:
"""
)