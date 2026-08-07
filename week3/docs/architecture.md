# System Architecture

## Overview

This project implements a production-oriented Retrieval-Augmented Generation (RAG) system capable of answering questions using an indexed knowledge base while supporting external tool execution through a modular AI agent.

The application follows a layered architecture that separates document processing, retrieval, language model interaction, agent orchestration, and utility components. Each module has a clearly defined responsibility, making the system easier to maintain, extend, and test.

---

# High-Level Architecture

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
                        Cross Encoder
                               │
                         Google Gemini
                               │
                               ▼
                           Final Answer
```

---

# Architectural Layers

The system is divided into several independent layers.

## 1. User Interface Layer

The entry point of the application is:

```
app.py
```

Responsibilities:

- Accept user queries
- Initialize the agent
- Initialize available tools
- Manage conversation memory
- Route requests to either tools or the RAG pipeline
- Display responses

---

## 2. Tool Layer

The tool layer enables the AI assistant to perform deterministic operations without invoking the retrieval pipeline.

Current tools include:

- Calculator Tool
- File Reader Tool

The Tool Executor checks whether a user request matches a supported tool and executes it before invoking the AI agent.

Benefits:

- Faster responses
- Reduced LLM usage
- Deterministic outputs
- Modular tool integration

---

## 3. Agent Layer

The AI agent is implemented using LangGraph.

Responsibilities:

- Route incoming queries
- Decide whether retrieval is necessary
- Execute document retrieval
- Generate grounded responses

The agent consists of three primary nodes:

- Router Node
- Retrieval Node
- Generation Node

The workflow is implemented as a directed state graph.

---

## 4. Retrieval Layer

The retrieval layer is responsible for finding relevant information from the indexed document collection.

Components include:

### Dense Retrieval

Implemented using:

- Google Gemini Embeddings
- FAISS Vector Database

This retrieves semantically similar documents.

### Sparse Retrieval

Implemented using BM25.

This retrieves keyword-based matches.

### Hybrid Retrieval

The outputs from dense and sparse retrieval are combined using Reciprocal Rank Fusion (RRF).

Hybrid retrieval improves both recall and robustness compared to either retrieval strategy alone.

---

## 5. Re-ranking Layer

Retrieved documents are passed through a Cross-Encoder reranker.

Responsibilities:

- Score retrieved documents using the full query-document pair
- Improve ranking quality
- Remove less relevant chunks

Only the highest-ranked documents are forwarded to the language model.

---

## 6. Generation Layer

Google Gemini generates the final response.

Instead of answering directly, the model receives:

- Retrieved context
- User question

The response is therefore grounded in the indexed knowledge base, reducing hallucinations.

---

# Document Processing Pipeline

Documents pass through several stages before becoming searchable.

```text
PDF / DOCX / Markdown / TXT
            │
            ▼
      Document Loader
            │
            ▼
         Chunking
            │
            ▼
      Embedding Model
            │
            ▼
      FAISS Vector Store
```

---

# Project Structure

```
src/
│
├── agents/
├── embeddings/
├── exceptions/
├── llms/
├── loaders/
├── memory/
├── processing/
├── prompts/
├── rag/
├── rerankers/
├── retrievers/
├── tools/
├── utils/
└── vectorstores/
```

Each module is responsible for a single concern, improving modularity and maintainability.

---

# Design Principles

The implementation follows several software engineering principles.

## Separation of Concerns

Each module performs one specific task.

Examples include:

- Retrieval
- Embeddings
- Chunking
- Tool execution
- Prompt management

---

## Modularity

Components can be replaced independently.

Examples:

- FAISS can be replaced with ChromaDB.
- Gemini can be replaced with another LLM.
- Additional tools can be registered without modifying existing logic.

---

## Extensibility

Abstract base classes are used throughout the project.

Examples include:

- BaseRetriever
- BaseEmbedding
- BaseLLM
- BaseTool
- BaseReranker

This allows new implementations to be added with minimal changes.

---

## Maintainability

The project structure promotes readability through:

- Type hints
- Modular packages
- Centralized configuration
- Structured logging
- Consistent naming conventions

---

# Summary

The architecture combines document processing, hybrid retrieval, reranking, LangGraph workflow orchestration, and tool execution into a modular Retrieval-Augmented Generation system.

Its layered design makes the project scalable, maintainable, and suitable for future enhancements such as additional tools, long-term memory, web search, or deployment as a web service.