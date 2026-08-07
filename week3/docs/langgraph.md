# LangGraph Implementation

## Overview

LangGraph is a framework for building stateful AI applications using graph-based workflows.

Unlike traditional sequential pipelines, LangGraph models an AI application as a directed graph where each node performs a specific task and communicates through a shared state.

For this project, LangGraph is used to orchestrate the Retrieval-Augmented Generation (RAG) workflow.

---

# Why LangGraph?

Traditional AI pipelines follow a fixed sequence of operations.

```
User
  │
  ▼
Retrieve
  │
  ▼
Generate
```

Although simple, this approach lacks flexibility because every query follows the same path.

LangGraph enables conditional execution.

```
                 START
                    │
                    ▼
               Router Node
               /         \
              /           \
       Retrieve        Generate
```

Only queries that require document retrieval execute the retrieval pipeline.

This reduces unnecessary retrieval operations and improves efficiency.

---

# Graph Components

The implementation consists of three nodes.

## Router Node

Responsibilities:

- Receive the user query.
- Decide whether retrieval is necessary.
- Select the next node.

Output:

- `retrieve`
- `generate`

The Router Node uses a lightweight Gemini model with a routing prompt.

---

## Retrieval Node

Executed only when the router selects the retrieval path.

Responsibilities:

- Retrieve relevant documents.
- Perform hybrid retrieval.
- Apply reranking.
- Build the context string.
- Update the shared state.

---

## Generation Node

Responsibilities:

- Generate the final response.
- Use retrieved context when available.
- Prevent hallucinations when no relevant documents are found.

---

# Shared State

All nodes communicate through a common `AgentState`.

The shared state contains:

| Field | Purpose |
|--------|---------|
| question | Current user query |
| results | Retrieved documents |
| context | Combined retrieval context |
| answer | Final generated response |
| metadata | Execution information |

Each node updates only the fields for which it is responsible.

This keeps node implementations independent and modular.

---

# Workflow

The implemented graph is:

```
START
   │
   ▼
Router
   │
   ├─────────────┐
   │             │
retrieve     generate
   │             │
   ▼             │
Retrieval        │
   │             │
   └──────┬──────┘
          ▼
     Generation
          │
          ▼
         END
```

---

# Routing Strategy

The Router LLM classifies user queries into two categories.

### Retrieval Required

Examples:

- What is a database?
- Explain normalization.
- What is primary key?
- Tell me about the Whack-a-Mole project.

These questions benefit from consulting the indexed knowledge base.

---

### Direct Generation

Examples:

- Hello
- Good morning
- Thank you
- Tell me a joke

These questions do not require document retrieval.

---

# Advantages

Using LangGraph provides several benefits.

## Dynamic Routing

The workflow adapts based on the user's query instead of following a fixed sequence.

---

## State Management

All nodes share a structured state, eliminating the need to pass multiple variables between functions.

---

## Modularity

Each node performs one clearly defined responsibility.

This makes the system easier to test, debug, and extend.

---

## Extensibility

Additional nodes can be added with minimal changes.

Examples include:

- Web Search Node
- Memory Node
- Planning Node
- Reflection Node
- Tool Selection Node

---

# Why LangGraph Instead of a Sequential Pipeline?

| Sequential Pipeline | LangGraph |
|---------------------|-----------|
| Fixed execution | Dynamic execution |
| No routing | Conditional routing |
| Limited flexibility | Easily extensible |
| Harder to maintain | Modular node architecture |
| Limited scalability | Designed for complex AI workflows |

---

# Current Limitations

The current implementation uses a relatively simple workflow.

Future versions could include:

- Long-term memory integration
- Multi-agent collaboration
- Web search capabilities
- Planning and reasoning nodes
- Human-in-the-loop approval

---

# Summary

LangGraph serves as the orchestration layer of the AI assistant.

By separating routing, retrieval, and generation into independent nodes connected through a shared state, the system remains modular, maintainable, and scalable. This design allows future enhancements to be incorporated with minimal changes to the existing workflow.