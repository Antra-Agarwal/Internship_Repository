"""
Evaluation queries for the Week 3 RAG System.
"""

TEST_QUERIES = [
    # -----------------------------
    # Direct Factual Questions
    # -----------------------------
    "What is a database?",
    "What is DBMS?",
    "Explain primary key.",
    "What is normalization?",
    "Explain SQL.",
    "What are the advantages of a database?",

    # -----------------------------
    # Multi-step Reasoning
    # -----------------------------
    "Why is a DBMS better than a file system?",
    "Explain the relationship between primary keys and normalization.",
    "Summarize the technical documentation.",
    "Which OOP concepts are used in the Whack-A-Mole project?",

    # -----------------------------
    # Out-of-Knowledge-Base
    # -----------------------------
    "What is an Operating System?",
    "Explain Computer Networks.",
    "What is Machine Learning?",
    "Who invented Python?",

    # -----------------------------
    # Calculator Tool
    # -----------------------------
    "25*(18+7)",
    "100/5+17",
    "(55-13)*6",

    # -----------------------------
    # File Reader Tool
    # -----------------------------
    "read sample.txt",
    "open sample.txt",
    "show sample.txt",
]