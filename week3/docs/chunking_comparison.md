# Chunking Strategy Comparison

## Introduction

Chunking is one of the most important stages in a Retrieval-Augmented Generation (RAG) pipeline. Large Language Models cannot process entire documents efficiently, so documents are divided into smaller chunks before generating embeddings and storing them in a vector database. The quality of chunking directly affects retrieval accuracy and the quality of generated responses.

This project implements and compares four chunking strategies to understand their strengths, limitations, and suitability for different use cases.

---

# Chunking Strategies

## 1. Fixed-Size Chunking

### Description

Fixed-size chunking divides a document into chunks of a predefined number of characters, regardless of sentence or paragraph boundaries.

### Advantages

* Simple to implement
* Fast execution
* Predictable chunk sizes
* Low computational overhead

### Limitations

* May split sentences or paragraphs
* Can reduce contextual coherence
* May negatively impact retrieval quality

### Suitable Use Cases

* Large-scale indexing
* Applications where speed is more important than semantic accuracy

---

## 2. Recursive Chunking

### Description

Recursive chunking attempts to preserve the natural structure of a document by splitting using separators such as paragraphs, line breaks, and sentences before falling back to character-level splitting.

### Advantages

* Better preserves document structure
* Produces more readable chunks
* Good balance between efficiency and context preservation

### Limitations

* Chunk sizes may vary
* Very small documents or pages may not require further splitting

### Suitable Use Cases

* General-purpose RAG systems
* Most production document processing pipelines

---

## 3. Custom Semantic Chunking

### Description

The custom semantic chunker groups sentences based on their semantic similarity. Sentence embeddings are generated, similarity scores are computed, and semantically related sentences are combined into meaningful chunks.

### Advantages

* Preserves semantic relationships
* Produces contextually coherent chunks
* Can improve retrieval quality for complex documents

### Limitations

* Computationally expensive
* Requires embedding generation before chunk creation
* Slower than traditional chunking methods

### Suitable Use Cases

* Knowledge bases
* Technical documentation
* Question-answering systems

---

## 4. LangChain Semantic Chunking

### Description

LangChain provides a built-in semantic chunking implementation that automatically determines chunk boundaries using embedding similarity.

### Advantages

* Well-tested implementation
* Easy integration with LangChain pipelines
* Produces high-quality semantic chunks

### Limitations

* Requires multiple embedding API calls
* Can consume API quotas quickly when processing large documents
* Performance depends on the selected embedding model

### Suitable Use Cases

* Production systems using managed embedding services
* Rapid development with the LangChain ecosystem

---

# Experimental Observations

The chunking strategies were evaluated using the same document and embedding configuration.

| Strategy                    | Observation                                                                                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fixed Chunking              | Produced consistent chunk sizes with minimal processing overhead.                                                                                                                                                |
| Recursive Chunking          | Preserved document structure effectively. Since the test document pages were smaller than the configured chunk size, each page remained as a single chunk.                                                       |
| Custom Semantic Chunking    | Generated more semantically meaningful chunks by grouping related sentences together, improving contextual coherence.                                                                                            |
| LangChain Semantic Chunking | Produced semantic chunks successfully but required significantly more embedding API calls. During testing with the free-tier Google Gemini embedding service, API quota limits were reached on larger documents. |

---

# Comparison Summary

| Feature                   | Fixed | Recursive | Custom Semantic | LangChain Semantic |
| ------------------------- | ----- | --------- | --------------- | ------------------ |
| Speed                     | High  | High      | Medium          | Medium             |
| Context Preservation      | Low   | Good      | Excellent       | Excellent          |
| Implementation Complexity | Low   | Medium    | High            | Low                |
| Embedding Required        | No    | No        | Yes             | Yes                |
| Computational Cost        | Low   | Low       | High            | High               |

---

# Final Recommendation

Each chunking strategy has its own strengths depending on the application.

* **Fixed Chunking** is suitable for simple and high-speed indexing tasks.
* **Recursive Chunking** provides a strong balance between efficiency and contextual preservation, making it an excellent default choice for most RAG systems.
* **Custom Semantic Chunking** offers better semantic coherence and is recommended when retrieval quality is more important than processing speed.
* **LangChain Semantic Chunking** is a robust production-ready implementation but requires careful management of embedding API usage due to higher computational cost.

For this project, **Recursive Chunking** is selected as the default chunking strategy because it provides an effective balance between performance, document structure preservation, and implementation simplicity. The semantic chunking implementations are retained for experimentation and future retrieval quality improvements.

---

# Conclusion

This comparison demonstrates that there is no universally best chunking strategy. The appropriate choice depends on the application's requirements, available computational resources, and desired retrieval quality. Implementing and evaluating multiple chunking approaches provides flexibility for future optimization of the RAG pipeline.
# Chunking Strategy Comparison

## Overview

Large Language Models cannot process entire documents efficiently because of context window limitations.

To enable efficient retrieval, documents are divided into smaller pieces called **chunks** before generating embeddings and storing them in the vector database.

This project implements and evaluates three chunking strategies:

- Fixed-size Chunking
- Recursive Chunking
- Semantic Chunking

The goal is to understand the advantages and limitations of each approach and select the most suitable strategy for the Retrieval-Augmented Generation (RAG) pipeline.

---

# Why Chunking?

Instead of embedding an entire document, the document is divided into manageable sections.

Benefits include:

- Improved retrieval accuracy
- Better embedding quality
- Reduced context size
- Faster similarity search
- More relevant responses

---

# Chunking Pipeline

```
Document
    │
    ▼
Document Loader
    │
    ▼
Chunking Strategy
    │
    ▼
Document Chunks
    │
    ▼
Embedding Generation
    │
    ▼
FAISS Vector Store
```

---

# 1. Fixed-Size Chunking

## Description

Fixed-size chunking divides documents into chunks containing a predefined number of characters.

Example:

```
Chunk Size = 500

Chunk 1
Characters 1–500

Chunk 2
Characters 501–1000

Chunk 3
Characters 1001–1500
```

---

## Advantages

- Simple implementation
- Fast execution
- Consistent chunk sizes
- Low computational cost

---

## Limitations

- May split sentences
- Can break paragraphs
- Ignores document structure
- Reduced semantic coherence

---

# 2. Recursive Chunking

## Description

Recursive chunking attempts to preserve document structure.

Instead of cutting strictly by character count, it recursively splits using separators such as:

- Paragraphs
- Blank lines
- Sentences
- Spaces

Only when necessary does it split by character length.

---

## Advantages

- Preserves semantic meaning
- Maintains paragraph boundaries
- Better retrieval quality
- More coherent context

---

## Limitations

- Slightly slower than fixed-size chunking
- Chunk sizes are less uniform

---

# 3. Semantic Chunking

## Description

Semantic chunking groups text based on meaning rather than character count.

Adjacent text segments are compared using embedding similarity.

Chunks are created when the semantic similarity between consecutive segments decreases significantly.

---

## Advantages

- High semantic coherence
- Natural topic boundaries
- Excellent retrieval quality

---

## Limitations

- Computationally expensive
- Requires additional embedding generation
- Slower indexing process

---

# Comparison

| Feature | Fixed | Recursive | Semantic |
|---------|:-----:|:---------:|:--------:|
| Speed | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| Simplicity | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ |
| Context Preservation | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Semantic Quality | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Retrieval Accuracy | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Computational Cost | Low | Medium | High |

---

# Selected Strategy

The production RAG pipeline uses **Recursive Chunking**.

Reasons:

- Preserves document structure
- Produces coherent chunks
- Balances retrieval quality and indexing speed
- Well suited for technical documentation
- Lower computational overhead than semantic chunking

Semantic chunking was implemented and evaluated for comparison but was not selected as the default due to its higher computational cost.

---

# Future Improvements

Possible enhancements include:

- Adaptive chunk sizes
- Hybrid chunking strategies
- Dynamic overlap selection
- Topic-aware chunking
- LLM-assisted chunking

---

# Summary

Three chunking strategies were implemented and evaluated.

- **Fixed-size chunking** provides simplicity and speed.
- **Recursive chunking** offers the best balance between efficiency and retrieval quality.
- **Semantic chunking** produces highly coherent chunks but incurs additional computational cost.

Based on these observations, **Recursive Chunking** was selected as the default strategy for the production RAG pipeline.