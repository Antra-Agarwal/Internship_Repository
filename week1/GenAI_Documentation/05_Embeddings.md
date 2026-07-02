# 05 – Embeddings

## What are Embeddings?

**Embeddings** are numerical representations of text, images, or other data that capture their meaning. They allow AI models to compare the similarity between different pieces of information.

Instead of storing words as plain text, an AI model converts them into vectors (lists of numbers).

---

## Why are Embeddings Needed?

Computers cannot understand human language directly. They process numbers rather than words.

Embeddings convert text into numerical vectors while preserving semantic meaning, allowing AI systems to identify similar words, sentences, or documents.

---

## How Do Embeddings Work?

```text id="i9kq4o"
Text
 │
 ▼
Embedding Model
 │
 ▼
Numerical Vector
 │
 ▼
Similarity Search
```

Text with similar meanings produces vectors that are close to each other in the vector space.

---

## Example

Consider the following words:

```text id="g7zjlwm"
Doctor
Nurse
Hospital
```

These words have related meanings, so their embeddings are located close to one another.

On the other hand,

```text id="p50u4o"
Doctor
Football
Pizza
```

have very different meanings, so their embeddings are farther apart.

---

## Applications of Embeddings

* Semantic Search
* Recommendation Systems
* Document Retrieval
* Question Answering
* Retrieval-Augmented Generation (RAG)

---

## Advantages

* Captures semantic meaning
* Enables similarity search
* Improves document retrieval
* Supports modern AI applications such as RAG

---

## Key Takeaways

* Embeddings convert data into numerical vectors.
* Similar meanings produce similar vectors.
* Embeddings are the foundation of semantic search and RAG systems.

---

## Summary

Embeddings allow AI systems to represent text as numerical vectors while preserving meaning. They play a crucial role in modern AI applications by enabling similarity search, document retrieval, and efficient information matching.
