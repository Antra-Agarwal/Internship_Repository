# Embedding Model Selection

## Overview

Embeddings are numerical vector representations of text that capture semantic meaning.

Instead of comparing words literally, embeddings allow the system to compare the meaning of documents and queries.

They form the foundation of semantic search in Retrieval-Augmented Generation (RAG) systems.

---

# Why Embeddings?

Traditional keyword search depends on exact word matching.

Example:

```
Document:
"Database Management Systems"

Query:
"What is DBMS?"
```

Although the document contains the answer, keyword search may fail because the words do not exactly match.

Embedding models solve this problem by mapping semantically similar text to nearby points in a high-dimensional vector space.

---

# Embedding Workflow

```
Document
    │
    ▼
Embedding Model
    │
    ▼
Vector Representation
    │
    ▼
FAISS Vector Database

----------------------------

User Question
      │
      ▼
Embedding Model
      │
      ▼
Query Vector
      │
      ▼
Similarity Search
      │
      ▼
Relevant Documents
```

---

# Selected Embedding Model

This project uses:

**Google Gemini Embedding 001**

The embedding model is accessed through the LangChain Google Generative AI integration.

---

# Why Gemini Embeddings?

The following factors influenced the selection.

## Semantic Quality

Gemini embeddings produce high-quality semantic representations suitable for Retrieval-Augmented Generation.

---

## Native Integration

The embedding model integrates seamlessly with:

- LangChain
- Google Gemini
- Existing LLM pipeline

---

## Consistent Provider

Using Gemini for both:

- Embedding generation
- Response generation

ensures compatibility throughout the pipeline.

---

## Large Embedding Dimension

The model produces high-dimensional vectors capable of representing complex semantic relationships between documents.

---

# Embedding Generation

Each document chunk is converted into an embedding before indexing.

```
Chunk 1
    │
    ▼
Embedding Vector

Chunk 2
    │
    ▼
Embedding Vector

Chunk 3
    │
    ▼
Embedding Vector
```

The resulting vectors are stored inside the FAISS vector database.

---

# Query Embedding

During retrieval, the user question follows the same embedding process.

```
User Question
       │
       ▼
Gemini Embedding Model
       │
       ▼
Query Vector
       │
       ▼
Similarity Search
```

This ensures documents and queries exist in the same semantic vector space.

---

# Similarity Search

FAISS compares the query embedding against all indexed document embeddings.

Documents with the highest similarity scores are returned as retrieval candidates.

These candidates are later improved using Hybrid Retrieval and Cross-Encoder reranking.

---

# Advantages

Using embeddings provides several benefits.

- Semantic understanding
- Synonym recognition
- Context-aware retrieval
- Improved recall
- Better retrieval quality than keyword matching alone

---

# Integration with the RAG Pipeline

The embedding model is used during two stages.

## Indexing Phase

```
Document
    │
    ▼
Chunking
    │
    ▼
Embedding Generation
    │
    ▼
FAISS Index
```

---

## Retrieval Phase

```
User Query
     │
     ▼
Embedding Generation
     │
     ▼
FAISS Search
     │
     ▼
Relevant Documents
```

---

# Future Improvements

Possible future enhancements include:

- Comparing multiple embedding models
- Domain-specific embeddings
- Multilingual embeddings
- Open-source embedding models
- Embedding benchmarking using retrieval metrics

---

# Summary

Embeddings enable semantic search by converting text into numerical vector representations.

The project uses **Google Gemini Embedding 001** to generate embeddings for both document chunks and user queries. These vectors are stored in FAISS and form the basis of the dense retrieval component of the RAG pipeline.