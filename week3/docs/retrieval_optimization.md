# Retrieval Optimization

## Overview

Retrieval quality is one of the most important factors affecting the performance of a Retrieval-Augmented Generation (RAG) system.

Even with high-quality embeddings, returning irrelevant documents can lead to inaccurate or incomplete responses.

To improve retrieval quality, several optimization techniques were implemented and evaluated in this project.

The following techniques were explored:

- Top-K Retrieval
- Similarity Score Thresholding
- Metadata Filtering
- Hybrid Retrieval
- Cross-Encoder Re-ranking

---

# Retrieval Pipeline

```
User Query
     │
     ▼
Embedding Generation
     │
     ▼
Dense Retrieval (FAISS)
     │
     ▼
Sparse Retrieval (BM25)
     │
     ▼
Reciprocal Rank Fusion
     │
     ▼
Cross Encoder Re-ranking
     │
     ▼
Top Ranked Documents
     │
     ▼
LLM Response Generation
```

---

# 1. Top-K Retrieval

## Description

Top-K retrieval limits the number of retrieved documents returned from the vector database.

Instead of returning every matching document, only the top **K** highest-scoring documents are selected.

Example:

```
Top-3

Document A
Document B
Document C
```

---

## Purpose

Top-K retrieval helps:

- Reduce irrelevant context
- Improve response quality
- Reduce prompt size
- Improve inference speed

---

## Observations

Different values of **K** were evaluated.

Small values produced concise context but occasionally missed useful information.

Large values increased context size and sometimes introduced irrelevant documents.

A balance between retrieval quality and efficiency was achieved by retrieving more candidates initially and selecting the highest-ranked results after reranking.

---

# 2. Similarity Score Thresholding

## Description

Similarity thresholding removes documents whose similarity score falls below a predefined value.

Only documents that satisfy the threshold are considered relevant.

---

## Purpose

This technique reduces noisy retrieval results and helps prevent unrelated context from being passed to the language model.

---

## Observations

Thresholding reduced irrelevant document retrieval but required careful tuning.

Very high thresholds occasionally filtered out useful documents, while low thresholds allowed less relevant context to pass through.

---

# 3. Metadata Filtering

## Description

Metadata filtering restricts retrieval to documents matching specific metadata fields.

Examples include:

- Source document
- File type
- Page number

---

## Purpose

Metadata filtering allows searches to be constrained to a subset of the indexed collection.

This is useful when users want results from a specific document or category.

---

## Observations

Metadata filtering significantly improved precision for targeted queries by eliminating unrelated documents before similarity search.

---

# 4. Hybrid Retrieval

## Description

Hybrid retrieval combines:

- Dense semantic retrieval using FAISS
- Sparse keyword retrieval using BM25

The results from both retrieval methods are merged using **Reciprocal Rank Fusion (RRF)**.

---

## Why Hybrid Retrieval?

Dense retrieval captures semantic similarity.

Sparse retrieval captures exact keyword matches.

Combining both methods improves retrieval robustness and recall.

---

## Advantages

- Better semantic understanding
- Improved keyword matching
- Higher retrieval accuracy
- Reduced dependence on a single retrieval strategy

---

# 5. Cross-Encoder Re-ranking

## Description

The retrieved candidate documents are re-ranked using a Cross-Encoder model.

Unlike embedding similarity, the Cross-Encoder evaluates the complete query-document pair to estimate relevance.

---

## Purpose

The reranker improves document ordering before context is passed to the language model.

Only the highest-ranked documents are included in the final prompt.

---

## Observations

Cross-Encoder reranking consistently improved retrieval quality by moving the most relevant documents to the top of the ranked list.

Although reranking increases inference time slightly, the improvement in answer quality justified the additional computation.

---

# Summary of Techniques

| Technique | Purpose | Benefit |
|-----------|---------|---------|
| Top-K Retrieval | Limit retrieved documents | Faster and more focused context |
| Similarity Threshold | Remove weak matches | Reduced retrieval noise |
| Metadata Filtering | Restrict search scope | Improved precision |
| Hybrid Retrieval | Combine dense and sparse search | Higher recall and robustness |
| Cross-Encoder Re-ranking | Improve document ordering | Better answer quality |

---

# Final Retrieval Strategy

The final production pipeline combines all major retrieval optimizations:

```
User Query
     │
     ▼
Embedding Generation
     │
     ▼
FAISS Dense Retrieval
     │
     ▼
BM25 Sparse Retrieval
     │
     ▼
Reciprocal Rank Fusion
     │
     ▼
Cross-Encoder Re-ranking
     │
     ▼
Top Documents
     │
     ▼
Gemini Response Generation
```

This hybrid retrieval pipeline provides a strong balance between retrieval accuracy, semantic understanding, and computational efficiency.

---

# Conclusion

Multiple retrieval optimization techniques were implemented and evaluated to improve the overall performance of the RAG system.

The combination of **Hybrid Retrieval**, **Reciprocal Rank Fusion**, and **Cross-Encoder Re-ranking** produced the most effective retrieval pipeline, resulting in more relevant context and higher-quality grounded responses.