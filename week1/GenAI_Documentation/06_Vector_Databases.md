# 06 – Vector Databases

## What is a Vector Database?

A **Vector Database** is a specialized database designed to store, manage, and search vector embeddings efficiently. Instead of searching for exact words, it searches for data with similar meanings.

Vector databases are an essential component of modern AI applications, especially Retrieval-Augmented Generation (RAG).

---

## Why are Vector Databases Needed?

After converting text into embeddings, the vectors need to be stored so they can be searched later.

Traditional databases search using exact matches, whereas vector databases perform **similarity searches**, allowing AI systems to retrieve information that is semantically related to the user's query.

---

## How Does a Vector Database Work?

```text id="7vf40o"
Documents
      │
      ▼
Generate Embeddings
      │
      ▼
Store in Vector Database
      │
      ▼
User Query
      │
      ▼
Convert Query to Embedding
      │
      ▼
Similarity Search
      │
      ▼
Return Most Relevant Documents
```

---

## Example

Suppose a user asks:

> "How do I reset my password?"

Even if the stored document contains the phrase:

> "Steps to change your account password"

the vector database can retrieve it because both sentences have similar meanings, even though the wording is different.

---

## Popular Vector Databases

| Vector Database | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| **FAISS**       | Open-source library developed by Meta for fast similarity search. |
| **Chroma**      | Lightweight vector database commonly used in RAG applications.    |
| **Pinecone**    | Managed cloud-based vector database.                              |
| **Weaviate**    | Open-source vector database with built-in AI capabilities.        |

---

## Applications

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* AI Chatbots
* Recommendation Systems
* Document Search
* Knowledge Management Systems

---

## Advantages

* Fast similarity search
* Retrieves information based on meaning rather than exact words
* Efficiently handles large collections of embeddings
* Improves the accuracy of AI applications

---

## Key Takeaways

* Vector databases store embeddings instead of plain text.
* They perform similarity searches using vector representations.
* They are an important part of RAG systems and semantic search applications.

---

## Summary

Vector databases enable AI systems to efficiently store and search embeddings based on semantic similarity. By retrieving the most relevant information instead of relying on exact keyword matches, they significantly improve the performance of RAG systems, AI chatbots, and intelligent search applications.
