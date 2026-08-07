# Production-Grade Retrieval-Augmented Generation (RAG) AI Agent

> A modular, production-quality Retrieval-Augmented Generation (RAG) system built using **LangGraph**, **LangChain**, **Google Gemini**, **FAISS**, **BM25**, and **Cross-Encoder Reranking**.

This project was developed as part of the **Week 3 Internship Assignment** at **Cognitio Analytics** to demonstrate the design and implementation of a complete RAG pipeline, hybrid retrieval, AI agent workflows, tool integration, evaluation, and production engineering practices.

---

# Features

## Document Processing

- PDF Loader
- DOCX Loader
- Markdown Loader
- TXT Loader
- Fixed-size Chunking
- Recursive Chunking
- Semantic Chunking
- Document Processing Pipeline

---

## Embeddings & Vector Search

- Google Gemini Embeddings
- FAISS Vector Database
- Dense Semantic Search
- Metadata Filtering
- Vector Store Persistence

---

## Retrieval Optimization

- Dense Retrieval
- BM25 Sparse Retrieval
- Hybrid Retrieval (Reciprocal Rank Fusion)
- Cross-Encoder Re-ranking
- Top-K Retrieval
- Similarity Thresholding

---

## AI Agent

Built using **LangGraph** with:

- Router Node
- Retrieval Node
- Generation Node
- Conditional Routing
- State Management

---

## Tool Calling

Integrated tools:

- Calculator Tool
- File Reader Tool
- Tool Registry
- Tool Executor

---

## Memory

- Short-term Conversation Memory
- Configurable Memory Window

---

## Production Features

- Modular Architecture
- Type Hints
- Structured Logging
- Error Handling
- Evaluation Framework
- Automated Test Suite

---

# System Architecture

```text
                           User
                             │
                             ▼
                          app.py
                             │
              ┌──────────────┴──────────────┐
              ▼                             ▼
        Tool Executor                 LangGraph Agent
              │                             │
      ┌───────┴────────┐              Router LLM
      ▼                ▼                   │
Calculator Tool   File Reader Tool         ▼
                                  Hybrid Retriever
                               ┌─────────┴─────────┐
                               ▼                   ▼
                            FAISS               BM25
                               │
                        Cross-Encoder
                               │
                         Google Gemini
                               │
                               ▼
                           Final Answer
```

---

# Technology Stack

| Category | Technologies |
|-----------|--------------|
| Programming Language | Python |
| LLM | Google Gemini |
| AI Framework | LangChain |
| Agent Framework | LangGraph |
| Embeddings | Gemini Embeddings |
| Vector Database | FAISS |
| Sparse Retrieval | BM25 |
| Hybrid Search | Reciprocal Rank Fusion |
| Re-ranking | Sentence Transformers Cross Encoder |
| Document Parsing | PyPDF, python-docx |
| Environment | python-dotenv |

---

# Project Structure

```
week3/
│
├── app.py
├── requirements.txt
├── README.md
│
├── data/
│   ├── documents/
│   ├── uploads/
│   └── vector_db/
│
├── docs/
│
├── evaluation/
│
├── scripts/
│
├── src/
│   ├── agents/
│   ├── embeddings/
│   ├── exceptions/
│   ├── llms/
│   ├── loaders/
│   ├── memory/
│   ├── processing/
│   ├── prompts/
│   ├── rag/
│   ├── rerankers/
│   ├── retrievers/
│   ├── tools/
│   ├── utils/
│   └── vectorstores/
│
└── tests/
```

---

# Installation

## Clone the repository

```bash
git clone <repository-url>
cd week3
```

## Create a virtual environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```
---

# Running the Application

## Step 1: Build the Vector Store

Before using the assistant, index the documents into the FAISS vector database.

```bash
python scripts/build_vector_store.py
```

This will:

- Load all supported documents
- Generate embeddings using Gemini
- Build the FAISS vector database
- Save the index to:

```
data/vector_db/
```

---

## Step 2: Start the AI Assistant

```bash
python app.py
```

Example:

```
============================================================
RAG AI ASSISTANT
============================================================

Loading agent...
Loading tools...

Ready!

You :
```

---

# Example Queries

## General Conversation

```
Hello
```

```
Who are you?
```

---

## Knowledge Base Questions

```
What is a database?
```

```
Explain normalization.
```

```
What are primary keys?
```

```
Tell me about the Whack-a-Mole project.
```

---

## Calculator Tool

```
25 * (18 + 5)
```

```
150 / 6
```

---

## File Reader Tool

```
Read sample.txt
```

---

# Supported Document Formats

| Format | Supported |
|---------|-----------|
| PDF | ✅ |
| DOCX | ✅ |
| Markdown | ✅ |
| TXT | ✅ |

---

# Retrieval Pipeline

The retrieval workflow consists of the following stages:

```
User Question
      │
      ▼
Router LLM
      │
      ▼
Hybrid Retrieval
      │
 ┌────┴────┐
 ▼         ▼
FAISS     BM25
      │
      ▼
Reciprocal Rank Fusion
      │
      ▼
Cross Encoder Reranker
      │
      ▼
Top Documents
      │
      ▼
Google Gemini
      │
      ▼
Grounded Response
```

---

# AI Agent Workflow

The LangGraph agent follows this workflow:

```
START
   │
   ▼
Router Node
   │
   ├──────────────┐
   │              │
retrieve      generate
   │              │
   ▼              │
Retrieval Node    │
   │              │
   └──────┬───────┘
          ▼
Generation Node
          │
          ▼
         END
```

---

# Running Tests

Individual modules can be tested independently.

Examples:

```bash
python tests/test_embeddings.py
```

```bash
python tests/test_vector_store.py
```

```bash
python tests/test_retriever.py
```

```bash
python tests/test_langgraph.py
```

```bash
python tests/test_calculator.py
```

```bash
python tests/test_file_reader.py
```

---

# Evaluation

Run the complete evaluation suite:

```bash
python evaluation/run_evaluation.py
```

The evaluation automatically measures:

- Retrieval quality
- Response quality
- Tool execution
- Latency
- Failure handling

Results are written to:

```
evaluation/results.md
```

A detailed analysis is available in:

```
evaluation/evaluation_report.md
```

---

# Project Highlights

This project demonstrates:

- End-to-End Retrieval-Augmented Generation
- Hybrid Retrieval (Dense + Sparse)
- Cross Encoder Re-ranking
- LangGraph-based AI Agent
- Tool Calling
- Conversation Memory
- Modular Software Design
- Structured Logging
- Automated Evaluation
- Production Engineering Practices

---

# Documentation

Additional technical documentation is available in the `docs/` directory.

| Document | Description |
|----------|-------------|
| architecture.md | Overall system architecture |
| agent_workflow.md | LangGraph workflow |
| chunking_comparison.md | Chunking strategy comparison |
| embeddings.md | Embedding model selection |
| retrieval_optimization.md | Retrieval optimization techniques |
| challenges_learnings.md | Challenges and lessons learned |
| langgraph.md | LangGraph implementation details |

---
# Future Improvements

The current implementation provides a modular and production-ready RAG system. Future enhancements may include:

- Long-term conversational memory
- Streaming LLM responses
- Multi-agent workflows
- Web search integration
- OCR support for scanned PDFs
- Image and multimodal document understanding
- Advanced evaluation metrics (Precision@K, Recall@K, MRR, nDCG)
- Docker deployment
- REST API using FastAPI
- Web interface using Streamlit or React
- Support for additional vector databases such as ChromaDB, PGVector, Pinecone, or Milvus

---

# Engineering Practices

This project follows several software engineering best practices:

- Modular architecture
- Separation of concerns
- Type hints throughout the codebase
- Abstract base classes for extensibility
- Configuration through environment variables
- Structured logging
- Comprehensive testing
- Evaluation-driven development
- Production-ready project structure

---

# Learning Outcomes

This project demonstrates practical understanding of:

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Vector Databases
- Embedding Models
- Hybrid Search
- Cross-Encoder Re-ranking
- LangGraph Workflows
- Tool Calling
- AI Agent Design
- Production Software Engineering

---

# Repository Highlights

✔ Multi-format document ingestion

✔ Three chunking strategies

✔ Gemini Embeddings

✔ FAISS Vector Database

✔ Hybrid Retrieval (Dense + Sparse)

✔ Cross-Encoder Re-ranking

✔ LangGraph-based AI Agent

✔ Tool Routing

✔ Calculator Tool

✔ File Reader Tool

✔ Conversation Memory

✔ Structured Logging

✔ Automated Evaluation Framework

✔ Modular Architecture

---

# Acknowledgements

This project was developed as part of the **Week 3 Internship** at **Cognitio Analytics**.

The implementation leverages the following open-source technologies:

- LangChain
- LangGraph
- Google Gemini
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- BM25 (rank-bm25)

Special thanks to the Cognitio Analytics team for providing the internship roadmap and learning objectives that guided the development of this project.

---

# License

This project was developed for educational and internship purposes.

---

# Author

**Antra Agarwal**

B.Tech Computer Science Engineering

Shiv Nadar Institution of Eminence

---

## Project Status

**Week 3 Internship Project — Completed**

This project demonstrates a complete Retrieval-Augmented Generation (RAG) pipeline with hybrid retrieval, LangGraph-based agent orchestration, tool integration, evaluation, and production engineering practices. It serves as a modular foundation for building scalable AI assistants and can be extended with additional tools, memory mechanisms, and deployment options.