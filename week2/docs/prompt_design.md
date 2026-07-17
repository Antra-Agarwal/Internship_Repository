# Prompt Design

## Overview

Prompt engineering is the process of designing effective instructions that guide a Large Language Model (LLM) to generate accurate, relevant, and well-structured responses.

During Week 2, prompt templates were used in all three AI applications to provide clear instructions to the Gemini model. Well-designed prompts improved the quality, consistency, and usefulness of the generated outputs.

---

# Project 1: AI Q&A Assistant

## Objective

Answer user questions accurately and clearly.

## Prompt Design

The prompt instructs the model to:

- Answer the user's question.
- Keep the explanation simple and easy to understand.
- Avoid unnecessary information.
- Respond naturally.

### Variables Used

- User Question

### Why This Prompt?

A simple prompt is sufficient because the application only performs question answering. The goal is to provide concise and informative responses while keeping the interaction user-friendly.

---

# Project 2: AI Email Generator

## Objective

Generate professional emails based on user requirements.

## Prompt Design

The prompt includes multiple user inputs:

- Email Type
- Recipient
- Tone
- Purpose
- Sender Name (optional)

The model is instructed to:

- Write a professional subject line.
- Generate a properly formatted email.
- Maintain the selected tone.
- Keep the content relevant to the provided purpose.
- End with an appropriate closing and signature.

### Variables Used

- Email Type
- Recipient
- Tone
- Purpose
- Sender Name

### Why This Prompt?

Providing structured information allows the model to generate emails that are personalized, professional, and context-aware while maintaining a consistent format.

---

# Project 3: AI Document Summarizer

## Objective

Generate concise summaries from text and PDF documents.

## Prompt Design

The prompt instructs the model to:

- Summarize the document.
- Preserve the key ideas.
- Use simple language.
- Present information using bullet points where appropriate.
- Adjust the level of detail based on the selected summary length.

### Variables Used

- Document Text
- Summary Length

### Why This Prompt?

The prompt focuses on preserving important information while reducing unnecessary details. Allowing the user to choose the summary length makes the application more flexible for different use cases.

---

# Prompt Engineering Techniques Used

Throughout the projects, the following prompt engineering practices were applied:

- Clear and specific instructions
- Dynamic prompts using Prompt Templates
- Variable substitution for user inputs
- Consistent output formatting
- Task-oriented prompts
- Simple language for better readability

---

# Learning Outcomes

Through designing prompts for these applications, I learned:

- How prompt wording influences AI responses.
- The importance of providing clear instructions.
- How Prompt Templates make prompts reusable.
- How structured prompts improve response consistency.
- How different prompts can be designed for different AI tasks.