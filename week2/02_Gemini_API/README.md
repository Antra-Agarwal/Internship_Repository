# Google Gemini API Integration

## Overview

This module demonstrates how to interact with Google's Gemini API using the latest `google-genai` Python SDK. It covers the fundamentals of connecting to a Large Language Model (LLM), generating text, using system instructions, and controlling model behavior with generation parameters.

---

## Objectives

- Connect to the Gemini API using an API key.
- Generate text responses from prompts.
- Understand system instructions.
- Experiment with generation parameters.
- Learn secure API key management using environment variables.

---

## Folder Structure

```
02_Gemini_API/
│
├── 01_basic_generation.py
├── 02_messages.py
├── 03_parameters.py
└── README.md
```

---

## Files

### 1. `01_basic_generation.py`

This program demonstrates the basic workflow of interacting with Gemini.

**Concepts Covered**

- Loading API key from `.env`
- Creating a Gemini client
- Sending a prompt
- Receiving and displaying the generated response

---

### 2. `02_messages.py`

This program demonstrates the use of **system instructions**.

**Concepts Covered**

- System Instructions
- User Prompt
- Prompt Engineering
- Controlling the behavior and tone of the model

Example:

- Friendly Teacher
- Interviewer
- Software Engineer

Changing the system instruction changes the style of the generated response without changing the user's prompt.

---

### 3. `03_parameters.py`

This program demonstrates how generation parameters affect model responses.

**Parameters Explored**

- **Temperature** – Controls creativity and randomness.
- **Max Output Tokens** – Limits the maximum length of the response.
- **Top-p** – Controls the diversity of generated tokens.
- **Top-k** – Limits the number of candidate tokens considered during generation.

---

## Technologies Used

- Python 3.13
- Google Gemini API
- google-genai SDK
- python-dotenv

---

## Project Workflow

```
User Prompt
      │
      ▼
Python Program
      │
      ▼
Gemini API
      │
      ▼
Gemini Model
      │
      ▼
Generated Response
      │
      ▼
Displayed to User
```

---

## Security

The API key is stored securely in a `.env` file and is **not uploaded to GitHub**.

Example:

```
GOOGLE_API_KEY=YOUR_API_KEY
```

The `.gitignore` file prevents the API key from being committed.

---

## Key Learnings

- Understanding how LLM APIs work.
- Secure API key management.
- Prompt engineering basics.
- Using system instructions.
- Controlling model behavior through generation parameters.
- Handling API responses in Python.

---

## Challenges Faced

- Setting up the Gemini API.
- Understanding API rate limits.
- Migrating from the deprecated `google-generativeai` package to the latest `google-genai` SDK.
- Handling API exceptions gracefully.

---

## Future Improvements

- Build conversational chat applications.
- Integrate LangChain.
- Add document summarization.
- Develop Retrieval-Augmented Generation (RAG) applications.

