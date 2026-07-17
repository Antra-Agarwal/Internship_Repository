# AI Document Summarizer

## Overview

The AI Document Summarizer is a command-line Generative AI application built using **Python**, **LangChain**, and **Google Gemini**. It reads text (`.txt`) and PDF (`.pdf`) documents, extracts their content, and generates concise AI-powered summaries.

This project demonstrates how Large Language Models (LLMs) can process and summarize documents efficiently.

---

## Features

- Supports both `.txt` and `.pdf` files
- Automatic file type detection
- AI-generated summaries
- Multiple summary lengths (Short, Medium, Detailed)
- Save summaries as text files
- Interactive command-line interface
- Secure API key management using `.env`
- Exception handling for invalid files and API errors

---

## Technologies Used

- Python 3
- Google Gemini API
- LangChain
- langchain-google-genai
- pypdf
- python-dotenv

---

## Project Structure

```
06_Document_Summarizer/
│
├── app.py
├── sample.txt
└── README.md
```

---

## Workflow

```
User
   │
   ▼
Select Document
   │
   ▼
Read File
(.txt / .pdf)
   │
   ▼
Extract Text
   │
   ▼
Prompt Template
   │
   ▼
Google Gemini
   │
   ▼
Summary
   │
   ▼
Display / Save
```

---

## Installation

```bash
pip install -r ../requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Run

```bash
python app.py
```

---

## Key Concepts Used

- Large Language Models
- Prompt Engineering
- LangChain
- File Handling
- PDF Processing
- Output Parsing
- Exception Handling

---

## Future Improvements

- Support Word documents
- Web interface using Streamlit
- Keyword extraction
- Multi-language summarization
- Export summaries as PDF

---

## Learning Outcomes

After completing this project, I learned how to:

- Read and process text and PDF files.
- Build AI-powered document summarization tools.
- Integrate LangChain with Gemini.
- Create modular Python applications.
- Handle file operations and API responses.

---

## Author

**Antra Agarwal**

B.Tech Computer Science Engineering