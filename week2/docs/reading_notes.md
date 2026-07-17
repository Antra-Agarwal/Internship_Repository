# Week 2 Reading Notes

## Overview

As part of Week 2, I studied several fundamental concepts used in Generative AI and Large Language Model (LLM) applications. These concepts provide the foundation for building AI-powered applications using APIs and frameworks like LangChain.

---

# 1. Tokens

## What are Tokens?

Tokens are the small units of text that an LLM processes instead of entire words or sentences.

A token can be:

- A complete word
- Part of a word
- A punctuation mark
- A number
- A special character

For example:

```
ChatGPT is amazing!
```

may be split into tokens similar to:

```
"Chat"
"GPT"
" is"
" amazing"
"!"
```

Different AI models use different tokenization methods.

## Why are Tokens Important?

Tokens determine:

- How much text a model can process
- API usage and pricing
- Response length
- Model performance

The larger the number of tokens, the more computation is required.

---

# 2. Context Window

## What is a Context Window?

The context window is the maximum number of tokens that an AI model can consider at one time.

It includes:

- System instructions
- User messages
- Conversation history
- Model responses

If the total number of tokens exceeds the context window, older content may be removed or ignored.

## Why is it Important?

A larger context window allows the model to:

- Understand longer conversations
- Process large documents
- Maintain context over multiple interactions
- Generate more coherent responses

---

# 3. Embeddings (Introduction)

## What are Embeddings?

Embeddings are numerical vector representations of text.

Instead of understanding words as plain text, AI converts them into vectors that capture their meaning.

For example:

```
Cat
Dog
Lion
```

have similar meanings and therefore have similar vector representations.

## Applications

Embeddings are commonly used for:

- Semantic search
- Recommendation systems
- Document retrieval
- Text similarity
- Retrieval-Augmented Generation (RAG)

---

# 4. Vector Databases (Overview)

## What is a Vector Database?

A vector database stores embeddings instead of traditional rows and columns.

It allows AI applications to quickly find information that is semantically similar to a user's query.

Popular vector databases include:

- Pinecone
- Chroma
- FAISS
- Weaviate
- Milvus

## Why are Vector Databases Used?

They help AI systems:

- Search similar documents efficiently
- Build RAG applications
- Retrieve relevant information from large datasets
- Improve response quality

---

# 5. API Rate Limits

## What are API Rate Limits?

API rate limits restrict how many requests a user or application can send within a specific period.

For example:

- 60 requests per minute
- 1,000 requests per day

These limits prevent servers from being overloaded and ensure fair usage.

## Best Practices

- Avoid sending unnecessary requests.
- Handle API errors gracefully.
- Retry requests after waiting if a rate limit is reached.
- Cache responses when appropriate.
- Monitor API usage to stay within limits.

---

# Key Learnings

After completing the reading assignment, I learned:

- How LLMs process text using tokens.
- Why context windows affect AI responses.
- How embeddings represent semantic meaning.
- The role of vector databases in modern AI applications.
- Why API rate limits exist and how to work within them.

These concepts helped me better understand how Large Language Models work internally and how they are used in real-world AI applications.