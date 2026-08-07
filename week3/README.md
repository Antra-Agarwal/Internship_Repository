
# Production-Grade Retrieval-Augmented Generation (RAG) AI Agent

> A production-quality **Retrieval-Augmented Generation (RAG)** system built using **LangGraph**, **LangChain**, **Google Gemini**, **FAISS**, **BM25**, and **Cross-Encoder Re-ranking**.

This project was developed as part of the **Week 3 Internship Assignment** at **Cognitio Analytics**. It demonstrates the implementation of a complete Retrieval-Augmented Generation pipeline, hybrid retrieval, AI agent orchestration, tool integration, evaluation, structured logging, and production engineering practices.

---

## Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Docker Deployment](#docker-deployment)
- [Running the Application](#running-the-application)
- [Example Queries](#example-queries)
- [Retrieval Pipeline](#retrieval-pipeline)
- [AI Agent Workflow](#ai-agent-workflow)
- [Running Tests](#running-tests)
- [Evaluation](#evaluation)
- [Documentation](#documentation)
- [Engineering Practices](#engineering-practices)
- [Learning Outcomes](#learning-outcomes)
- [Repository Highlights](#repository-highlights)
- [Future Improvements](#future-improvements)
- [Acknowledgements](#acknowledgements)
- [License](#license)
- [Author](#author)
- [Project Status](#project-status)

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
- Automated Document Processing Pipeline

---

## Embeddings & Vector Search

- Google Gemini Embeddings
- FAISS Vector Database
- Dense Semantic Search
- Metadata Filtering
- Persistent Vector Storage

---

## Retrieval Optimization

- Dense Vector Retrieval
- BM25 Sparse Retrieval
- Hybrid Retrieval using Reciprocal Rank Fusion (RRF)
- Cross-Encoder Re-ranking
- Top-K Retrieval
- Similarity Score Thresholding

---

## AI Agent

Built using **LangGraph** with:

- Router Node
- Retrieval Node
- Generation Node
- Shared State Management
- Conditional Routing

---

## Tool Calling

Integrated tools include:

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
- Automated Evaluation
- Dockerized Deployment
- Comprehensive Technical Documentation
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
                    Cross-Encoder Re-ranker
                               │
                         Google Gemini
                               │
                               ▼
                           Final Answer
```

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| LLM | Google Gemini |
| AI Framework | LangChain |
| Agent Framework | LangGraph |
| Embeddings | Gemini Embeddings |
| Vector Database | FAISS |
| Sparse Retrieval | BM25 |
| Hybrid Retrieval | Reciprocal Rank Fusion |
| Re-ranking | Sentence Transformers Cross-Encoder |
| Document Parsing | PyPDF, python-docx |
| Environment Management | python-dotenv |
| Containerization | Docker & Docker Compose |

---

# Project Structure

```text
week3/
│
├── app.py
├── Dockerfile
├── docker-compose.yml
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

## 1. Clone the Repository

```bash
git clone <repository-url>
cd week3
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

# Docker Deployment

The application can be executed entirely inside Docker without manually installing Python or project dependencies.

## Prerequisites

Install:

- Docker Desktop
- Docker Compose

Verify the installation:

```bash
docker --version
docker compose version
```

---

## Build the Docker Image

```bash
docker compose build
```

This command:

- Builds the application image
- Installs all dependencies
- Copies the project into the container
- Prepares the runtime environment

---

## Run the Application

```bash
docker compose up
```

Expected output:

```text
============================================================
RAG AI ASSISTANT
============================================================

Loading agent...
Loading tools...

Application ready.
```

---

## Stop the Container

Press:

```text
Ctrl + C
```

Then remove the stopped container:

```bash
docker compose down
```

---

## Rebuild After Changes

Whenever dependencies or source files change:

```bash
docker compose up --build
```

---

## Docker Files

| File | Purpose |
|------|---------|
| Dockerfile | Defines the application image |
| docker-compose.yml | Configures and runs the container |
| .dockerignore | Excludes unnecessary files from the build context |

---

## Volume Mapping

The project mounts the local `data/` directory into the container.

Benefits:

- Persistent FAISS vector database
- Persistent uploaded documents
- No need to rebuild the index after restarting the container

---

## Environment Variables

Docker automatically loads the `.env` file specified in `docker-compose.yml`.

Example:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

No additional Docker configuration is required.

---
# Running the Application

## Step 1: Build the Vector Database

Before querying the knowledge base, documents must be indexed into the FAISS vector store.

Run:

```bash
python scripts/build_vector_store.py
```

This process performs the following steps:

1. Loads supported documents from `data/documents/`
2. Splits documents into chunks
3. Generates embeddings using Google Gemini
4. Stores embeddings inside the FAISS vector database

The generated index is stored in:

```text
data/vector_db/
```

---

## Step 2: Start the AI Assistant

Run:

```bash
python app.py
```

Expected output:

```text
============================================================
RAG AI ASSISTANT
============================================================

Loading agent...
Loading tools...

Application ready.
```

The assistant is now ready to answer questions.

---

# Example Queries

## General Conversation

```
Hello
```

```
Who are you?
```

```
Tell me something about yourself.
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
What is database normalization?
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

```
sqrt(144)
```

---

## File Reader Tool

```
Read sample.txt
```

```
Open sample.txt
```

---

# Supported Document Formats

| Format | Supported |
|----------|-----------|
| PDF | ✅ |
| DOCX | ✅ |
| Markdown | ✅ |
| TXT | ✅ |

---

# Retrieval Pipeline

The Retrieval-Augmented Generation pipeline consists of several stages.

```text
User Question
      │
      ▼
Router LLM
      │
      ▼
Hybrid Retriever
      │
 ┌────┴────┐
 ▼         ▼
FAISS     BM25
      │
      ▼
Reciprocal Rank Fusion
      │
      ▼
Cross-Encoder Re-ranking
      │
      ▼
Top Ranked Documents
      │
      ▼
Google Gemini
      │
      ▼
Grounded Response
```

---

## Retrieval Process

The retrieval workflow performs the following steps:

1. Convert the user query into an embedding.
2. Perform dense retrieval using FAISS.
3. Perform sparse retrieval using BM25.
4. Merge results using Reciprocal Rank Fusion.
5. Re-rank retrieved documents using a Cross-Encoder.
6. Select the highest-ranked document chunks.
7. Generate a grounded response using Gemini.

This combination significantly improves retrieval quality compared to using dense retrieval alone.

---

# AI Agent Workflow

The application uses **LangGraph** to orchestrate the Retrieval-Augmented Generation workflow.

```text
                     START
                       │
                       ▼
                 Router Node
                  /        \
                 /          \
        retrieve            generate
            │                  │
            ▼                  │
     Retrieval Node            │
            │                  │
            └────────┬─────────┘
                     ▼
             Generation Node
                     │
                     ▼
                    END
```

---

## Router Node

The Router Node determines whether the user's request requires retrieval.

Examples requiring retrieval:

```
What is a database?
```

```
Explain normalization.
```

Examples that bypass retrieval:

```
Hello
```

```
Thank you
```

---

## Retrieval Node

The Retrieval Node performs:

- Hybrid Retrieval
- Cross-Encoder Re-ranking
- Context Construction

The retrieved context is then passed to the Generation Node.

---

## Generation Node

The Generation Node generates the final response.

Two execution paths are supported:

### Retrieved Context Available

Gemini receives:

- Retrieved Context
- User Question

and generates a grounded response.

---

### No Relevant Documents Found

If retrieval does not return relevant context, the assistant responds with:

```
I don't know based on the provided documents.
```

This behavior reduces hallucinations and ensures responses remain grounded in the indexed knowledge base.

---

# Running Tests

Each component can be tested independently.

Examples:

```bash
python tests/test_chunking.py
```

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

```bash
python tests/test_tool_executor.py
```

---

# Evaluation

The project includes an automated evaluation framework.

Run:

```bash
python evaluation/run_evaluation.py
```

The evaluation measures:

- Retrieval quality
- Response quality
- Tool execution
- Latency
- Failure scenarios

Evaluation outputs are written to:

```text
evaluation/results.md
```

A detailed analysis is available in:

```text
evaluation/evaluation_report.md
```

---

# Evaluation Categories

The evaluation suite contains representative queries covering:

- Direct factual questions
- Multi-step reasoning
- Questions outside the knowledge base
- Calculator Tool execution
- File Reader Tool execution
- General conversation
- Failure scenarios

This helps assess both retrieval performance and overall agent behavior.

---

# Project Highlights

This project demonstrates:

- End-to-End Retrieval-Augmented Generation
- Hybrid Dense + Sparse Retrieval
- Reciprocal Rank Fusion
- Cross-Encoder Re-ranking
- LangGraph-based AI Agent
- Tool Calling
- Conversation Memory
- Structured Logging
- Automated Evaluation
- Dockerized Deployment
- Production Engineering Practices

---
# Documentation

Detailed technical documentation is available in the `docs/` directory.

| Document | Description |
|----------|-------------|
| architecture.md | Overall system architecture |
| agent_workflow.md | LangGraph workflow and execution |
| langgraph.md | LangGraph implementation details |
| embeddings.md | Embedding model selection and semantic search |
| chunking_comparison.md | Comparison of chunking strategies |
| retrieval_optimization.md | Hybrid retrieval and optimization techniques |
| challenges_learnings.md | Challenges faced and lessons learned |

---

# Engineering Practices

The project follows modern software engineering principles to improve maintainability, extensibility, and code quality.

## Software Design

- Modular architecture
- Separation of concerns
- Object-Oriented Design
- Abstract Base Classes
- Dependency Injection
- Configurable components

---

## Code Quality

- Type hints
- Comprehensive docstrings
- Structured logging
- Error handling
- Configuration through `.env`
- Reusable utility modules

---

## Testing

The project includes dedicated tests for individual modules including:

- Document Processing
- Embedding Generation
- Vector Store
- Retrieval
- LangGraph Workflow
- Calculator Tool
- File Reader Tool
- Tool Executor
- Complete RAG Pipeline

---

## Deployment

The application supports:

- Local execution
- Docker deployment
- Docker Compose orchestration

---

# Learning Outcomes

This project demonstrates practical understanding of:

## Retrieval-Augmented Generation

- Document ingestion
- Chunking
- Embeddings
- Vector databases
- Context retrieval
- Grounded response generation

---

## Information Retrieval

- Dense Retrieval
- Sparse Retrieval
- Hybrid Search
- Reciprocal Rank Fusion
- Cross-Encoder Re-ranking

---

## AI Agents

- LangGraph
- Graph-based workflows
- State management
- Conditional routing
- Tool integration
- Conversation memory

---

## Production Engineering

- Modular architecture
- Logging
- Error handling
- Evaluation framework
- Docker
- Documentation

---

# Repository Highlights

✔ Multi-format document ingestion

✔ Three chunking strategies

✔ Google Gemini Embeddings

✔ FAISS Vector Database

✔ BM25 Sparse Retrieval

✔ Hybrid Retrieval

✔ Reciprocal Rank Fusion

✔ Cross-Encoder Re-ranking

✔ LangGraph AI Agent

✔ Router Node

✔ Retrieval Node

✔ Generation Node

✔ Calculator Tool

✔ File Reader Tool

✔ Conversation Memory

✔ Structured Logging

✔ Automated Evaluation Framework

✔ Dockerized Deployment

✔ Production-Ready Modular Architecture

---

# Future Improvements

Although the current implementation provides a complete production-oriented RAG system, several future enhancements are possible.

## AI Capabilities

- Long-term conversational memory
- Multi-agent collaboration
- Planning and reasoning agents
- Reflection and self-correction
- Web search integration

---

## Retrieval

- Adaptive chunking
- Additional embedding models
- Advanced retrieval metrics
- Query expansion
- Vector database benchmarking

---

## Deployment

- FastAPI REST API
- Streamlit web interface
- React frontend
- Kubernetes deployment
- CI/CD using GitHub Actions

---

## Monitoring

- LLM usage analytics
- Token tracking
- Performance dashboards
- Observability
- Production monitoring

---

# Acknowledgements

This project was developed as part of the **Week 3 Internship** at **Cognitio Analytics**.

The implementation makes use of several excellent open-source projects, including:

- LangChain
- LangGraph
- Google Gemini
- FAISS
- Sentence Transformers
- Hugging Face Transformers
- rank-bm25
- PyPDF
- python-docx

Special thanks to the Cognitio Analytics team for providing the internship roadmap and learning objectives that guided the development of this project.

---

# License

This repository was developed for educational and internship purposes.

---

# Author

**Antra Agarwal**

B.Tech – Computer Science Engineering

Shiv Nadar Institution of Eminence

---

# Project Status

## ✅ Week 3 Internship Project — Completed

### Deliverables Completed

- Complete Document Processing Pipeline
- Multiple Chunking Strategies
- Google Gemini Embeddings
- FAISS Vector Database
- Hybrid Retrieval
- Cross-Encoder Re-ranking
- LangGraph AI Agent
- Tool Calling Framework
- Conversation Memory
- Automated Evaluation
- Technical Documentation
- Dockerized Deployment
- Production Engineering Practices

The project demonstrates a complete Retrieval-Augmented Generation (RAG) system capable of indexing documents, retrieving relevant context using hybrid search, executing external tools, orchestrating workflows with LangGraph, and generating grounded responses using Google Gemini.

The modular architecture and production-oriented design make the project suitable as a foundation for future AI assistants and enterprise GenAI applications.

---

## Repository Summary

This project showcases the implementation of a production-grade Retrieval-Augmented Generation (RAG) AI assistant developed using modern AI frameworks and software engineering best practices. It combines document ingestion, semantic retrieval, hybrid search, AI agent orchestration, external tool execution, evaluation, logging, documentation, and Dockerized deployment into a scalable and extensible architecture.