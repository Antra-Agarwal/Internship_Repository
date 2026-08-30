# Week 4 RAG Evaluation Report

## Overview

This report compares the Week 3 baseline RAG pipeline
with the Week 4 Advanced RAG pipeline.

The evaluation dataset contains:

- 36 test questions
- Simple factual questions
- Multi-document questions
- Reasoning questions
- Ambiguous questions
- Outside-knowledge-base questions
- Irrelevant-information questions

## Evaluation Metrics

### Retrieval Relevance

Measures whether expected document sources were retrieved.

### Context Relevance

Measures lexical overlap between the question and retrieved context.

### Answer Correctness

Measures lexical similarity with the expected answer for supported
questions and correct refusal behavior for unsupported questions.

### Faithfulness

Measures how much of the generated answer vocabulary occurs
in the retrieved context.

### Hallucination Rate

Estimated as:

`1 - Faithfulness`

### Source Accuracy

Measures whether the expected source documents were represented
in the final returned sources.

### Latency

Average end-to-end response time.

---

## Week 3 vs Week 4

| Metric | Week 3 | Week 4 |
|---|---:|---:|
| Questions | 2 | 2 |
| Retrieval relevance | 100.00% | 50.00% |
| Context relevance | 37.50% | 67.50% |
| Answer correctness | 50.00% | 100.00% |
| Faithfulness | 33.34% | 78.57% |
| Hallucination rate | 66.66% | 21.43% |
| Source accuracy | 100.00% | 50.00% |
| Average latency | 7.509s | 36.517s |
| Evaluation errors | 0 | 0 |

---

## Week 4 Features

The Week 4 pipeline includes:

1. Query transformation
2. Multi-query retrieval
3. Metadata filtering
4. Hybrid dense + sparse retrieval
5. Reciprocal Rank Fusion
6. Cross-encoder reranking
7. Context compression through final-k selection
8. Context validation
9. Source citations
10. Explicit unsupported-question handling

---

## Evaluation Design

The evaluator intentionally avoids making separate LLM calls
for individual evaluation metrics.

This keeps the evaluation deterministic and prevents unnecessary
consumption of the Gemini API quota.

The only LLM calls are the calls required by the RAG systems
themselves.

The Week 4 evaluator also performs retrieval exactly once per
question. The retrieved results are reused for context validation,
answer generation, and evaluation metrics.

---

## Important Limitation

The faithfulness and context-relevance metrics are deterministic
lexical metrics.

They are useful as lightweight evaluation signals but should not
be interpreted as equivalent to a semantic LLM judge.

---

## Output

Detailed per-question results:

`evaluation_results.csv`

Human-readable report:

`evaluation_report.md`
