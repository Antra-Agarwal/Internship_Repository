# 02 – Large Language Models (LLMs)

## What is a Large Language Model (LLM)?

A **Large Language Model (LLM)** is an Artificial Intelligence model trained on massive amounts of text data to understand and generate human-like language. LLMs can answer questions, write code, summarize documents, translate languages, and perform many other language-related tasks.

Popular LLMs include **GPT**, **Google Gemini**, **Claude**, and **Llama**.

---

## How Does an LLM Work?

At a high level, an LLM follows these steps:

```text id="6n65m2"
User Prompt
      │
      ▼
Tokenization
      │
      ▼
Model Processes Tokens
      │
      ▼
Predicts the Next Token
      │
      ▼
Generates Response
```

Instead of memorizing answers, an LLM predicts one token at a time based on patterns learned during training.

---

## What are Tokens?

A **token** is the basic unit of text processed by an LLM. A token can be a word, part of a word, punctuation mark, or symbol.

For example:

```text id="sh1jr8"
Sentence:
I love programming.

Possible Tokens:
"I" | "love" | "program" | "ming" | "."
```

LLMs process tokens rather than complete words or sentences.

---

## Context Window

The **context window** is the maximum amount of text (measured in tokens) that an LLM can consider while generating a response.

A larger context window allows the model to remember more information from the conversation or document.

---

## Temperature

**Temperature** controls the randomness of an LLM's responses.

* **Low Temperature (0–0.3):** More focused and consistent answers.
* **Medium Temperature (0.5–0.7):** Balanced responses.
* **High Temperature (0.8–1.0):** More creative and varied outputs.

---

## Applications of LLMs

* Chatbots and virtual assistants
* Code generation
* Text summarization
* Language translation
* Content creation
* Question answering
* Document analysis

---

## Limitations

* Can produce incorrect information (hallucinations)
* Limited by the context window
* Sensitive to prompt quality
* May reflect biases from training data

---

## Key Takeaways

* LLMs are trained on massive text datasets.
* They generate responses by predicting one token at a time.
* Tokens are the basic units processed by the model.
* Temperature controls creativity, while the context window determines how much information the model can remember.
* LLMs are widely used for text generation, coding, translation, summarization, and conversational AI.

---

## Summary

Large Language Models are the foundation of modern Generative AI applications. Their ability to understand and generate natural language has enabled intelligent chatbots, coding assistants, document summarization, and many other AI-powered applications used across industries today.
