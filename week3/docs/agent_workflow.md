# Agent Workflow

## Overview

The AI assistant is implemented using **LangGraph**, a framework for building stateful, graph-based AI workflows.

Unlike a traditional sequential pipeline, LangGraph represents the agent as a directed graph where each node performs a specific task and updates a shared state.

The workflow allows the system to dynamically decide whether document retrieval is required before generating a response.

---

# Workflow Diagram

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

# Shared State

All nodes communicate through a shared state object (`AgentState`).

The state contains:

| Field | Description |
|--------|-------------|
| question | User's input query |
| results | Retrieved documents |
| context | Combined retrieval context |
| answer | Final generated response |
| metadata | Execution details (route, retriever, reranker, etc.) |

Each node reads the existing state, performs its task, updates the relevant fields, and passes the updated state to the next node.

---

# Router Node

The Router Node is the entry point of the workflow.

Responsibilities:

- Receive the user's question
- Decide whether retrieval is necessary
- Choose the next node

The router uses a lightweight Gemini model with a routing prompt to classify the query into one of two categories:

### Retrieve

Selected for:

- Factual questions
- Technical concepts
- Educational queries
- Questions about indexed documents
- Any query that requires grounded information

Example:

```
What is a database?
```

---

### Generate

Selected for:

- Greetings
- Small talk
- Introductions
- Casual conversation
- Creative requests

Example:

```
Hello
```

The Router Node updates the execution metadata with the selected route.

---

# Retrieval Node

The Retrieval Node is executed only when the router selects the **retrieve** path.

Responsibilities:

1. Retrieve relevant document chunks
2. Apply Hybrid Retrieval
3. Re-rank retrieved documents
4. Construct the context string
5. Update the shared state

The retrieval pipeline consists of:

```text
Question
    │
    ▼
Hybrid Retriever
    │
 ┌──┴──┐
 ▼     ▼
FAISS BM25
    │
    ▼
Reciprocal Rank Fusion
    │
    ▼
Cross Encoder
    │
    ▼
Top Documents
```

The highest-ranked documents are combined into a single context passed to the Generation Node.

---

# Generation Node

The Generation Node is responsible for producing the final response.

Two execution paths are possible:

### Retrieved Context Available

The node constructs a Retrieval-Augmented Generation (RAG) prompt containing:

- Retrieved context
- User question

Gemini then generates a grounded response based only on the supplied context.

---

### No Retrieved Context

If retrieval fails to find relevant information, the node returns a controlled response indicating that the answer is not available in the indexed knowledge base.

This behavior helps reduce hallucinations by avoiding unsupported answers.

---

# Execution Metadata

During execution, metadata is collected to assist with debugging and evaluation.

Examples include:

- Selected route
- Retrieval success
- Number of retrieved documents
- Retriever used
- Reranker used
- Generator model

This metadata is useful for performance analysis and structured logging.

---

# Benefits of the Workflow

The LangGraph-based design provides several advantages:

- Dynamic routing based on query type
- Clear separation of responsibilities
- Modular node implementation
- Easy extensibility
- Improved maintainability
- Support for future multi-step reasoning

---

# Future Extensions

The current workflow can be extended with additional nodes, such as:

- Web Search Node
- Long-Term Memory Node
- Planning Node
- Tool Selection Node
- Multi-Agent Collaboration
- Reflection and Self-Correction

These additions can be integrated without modifying the existing node implementations, demonstrating the flexibility of the graph-based architecture.

---

# Summary

The LangGraph workflow enables the assistant to intelligently choose between direct response generation and retrieval-augmented generation.

By separating routing, retrieval, and generation into independent nodes with a shared state, the system remains modular, extensible, and well-suited for production-quality AI applications.