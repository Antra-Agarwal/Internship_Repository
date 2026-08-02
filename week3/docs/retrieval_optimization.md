# Retrieval Optimization

## 1. Top-K Retrieval
### Goal
Retrieve different numbers of candidate documents.

### Observation
- Top-K = 1 returned only the most relevant chunk.
- Increasing Top-K provided more context.
- Larger values also introduced less relevant documents.

### Conclusion
Top-K = 3–5 provided the best balance between relevance and context.

---

## 2. Similarity Score Thresholding

### Goal
Filter documents whose similarity score is below a chosen threshold.

### Observation
- Lower thresholds removed noisy results.
- Very strict thresholds sometimes returned no documents.
- Relaxed thresholds increased recall but introduced irrelevant chunks.

### Conclusion
A moderate threshold produced the best retrieval quality.

---

## 3. Metadata Filtering

### Goal
Restrict retrieval to documents matching metadata (e.g., source).

### Observation
- Successfully searched within a specific document.
- Useful for multi-document knowledge bases.
- Reduced irrelevant cross-document matches.

### Conclusion
Metadata filtering improves precision when document source is known.

---

## 4. Hybrid Search (Dense + BM25 + RRF)

### Goal
Combine semantic retrieval with keyword retrieval.

### Observation
- Dense retrieval captured semantic meaning.
- BM25 captured exact keyword matches.
- Reciprocal Rank Fusion combined strengths of both.

### Conclusion
Hybrid retrieval produced more robust rankings than either method alone.

---

## 5. Cross-Encoder Re-ranking

### Goal
Reorder retrieved documents using a cross-encoder.

### Observation
- Correct document moved to the top.
- Less relevant chunks were demoted.
- Improved final context sent to the LLM.

### Conclusion
Re-ranking significantly improved the quality of retrieved context before generation.

---

# Overall Findings

| Technique | Primary Benefit |
|-----------|-----------------|
| Top-K | Controls retrieval breadth |
| Thresholding | Filters low-quality matches |
| Metadata Filtering | Restricts search scope |
| Hybrid Search | Combines semantic and keyword retrieval |
| Re-ranking | Improves final ranking accuracy |

## Final Recommendation

The best-performing retrieval pipeline was:

Retriever (Top-10)
→ Metadata Filtering (optional)
→ Hybrid Search (Dense + BM25 using RRF)
→ Cross-Encoder Re-ranking (Top-3)
→ LLM