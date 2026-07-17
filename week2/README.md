# Week 2: Building Your First GenAI Applications

## Overview

This repository contains the work completed during **Week 2** of my Generative AI internship. The objective of this week was to gain hands-on experience in building AI-powered applications using **Large Language Models (LLMs)** and **LangChain**.

The week covered Python concepts, working with LLM APIs, learning LangChain fundamentals, building practical AI applications, and documenting key concepts related to Generative AI.

---

## Objectives

- Strengthen advanced Python programming skills.
- Learn how to interact with Large Language Models using APIs.
- Understand the core components of LangChain.
- Build practical AI applications.
- Practice Git and GitHub workflows.
- Learn fundamental concepts used in modern AI systems.

---

## Technologies Used

- Python 3
- Google Gemini API
- LangChain
- LangChain Google Generative AI
- Python Dotenv
- PyPDF
- Git & GitHub

---

## Folder Structure

```text
Week2/
│
├── README.md
├── requirements.txt
│
├── 01_Python_Refresher/
├── 02_Gemini_API/
├── 03_LangChain/
├── 04_AI_QA_Assistant/
├── 05_AI_Email_Generator/
├── 06_Document_Summarizer/
│
└── docs/
    ├── reading_notes.md
    ├── prompt_design.md
    └── challenges_learnings.md
```

---

# Tasks Completed

## 1. Python Refresher

Covered important Python concepts required for AI application development:

- File Handling
- Virtual Environments
- APIs and JSON
- Classes and Object-Oriented Programming
- Exception Handling

---

## 2. Working with LLM APIs

Learned how to interact with Google Gemini using Python.

Topics covered:

- API integration
- Prompt-based text generation
- System and user instructions
- Model parameters
- Secure API key management using environment variables

---

## 3. LangChain Fundamentals

Explored the core components of LangChain:

- Chat Models
- Prompt Templates
- Output Parsers
- Chains

These components were later used to build AI-powered applications.

---

# Mini Projects

## Project 1: AI Q&A Assistant

A command-line application that answers user questions using Google Gemini.

### Features

- Interactive question answering
- Prompt Templates
- LangChain pipeline
- Error handling
- Clean command-line interface

---

## Project 2: AI Email Generator

A command-line application that generates professional emails based on user requirements.

### Features

- Multiple email types
- Custom email type support
- Tone selection
- AI-generated subject and email body
- Save generated emails as text files

---

## Project 3: AI Document Summarizer

A command-line application that summarizes text and PDF documents.

### Features

- Support for TXT and PDF files
- Automatic file type detection
- Multiple summary lengths
- AI-generated summaries
- Save summaries as text files

---

# Documentation

Additional documentation created during Week 2:

| Document | Description |
|----------|-------------|
| `reading_notes.md` | Notes on Tokens, Context Windows, Embeddings, Vector Databases, and API Rate Limits |
| `prompt_design.md` | Prompt engineering approach used in each project |
| `challenges_learnings.md` | Challenges encountered and key learnings throughout the week |

---

# Skills Developed

## Programming

- Python
- File Handling
- Object-Oriented Programming
- Exception Handling

## AI & LLMs

- Large Language Models (LLMs)
- Google Gemini API
- Prompt Engineering
- LangChain
- Chat Models
- Prompt Templates
- Output Parsers

## Development Tools

- Git
- GitHub
- Virtual Environments
- VS Code

---

# Key Learnings

During Week 2, I learned how to:

- Build AI-powered applications using LLMs.
- Integrate Google Gemini into Python applications.
- Design effective prompts using Prompt Templates.
- Build reusable LangChain pipelines.
- Process text and PDF documents.
- Handle API responses and errors.
- Organize AI projects using modular programming practices.
- Maintain project documentation using Markdown.
- Use Git and GitHub for version control.

---

# How to Run the Projects

1. Clone the repository.

```bash
git clone <repository-url>
```

2. Navigate to the Week 2 directory.

```bash
cd Internship/Week2
```

3. Install the required dependencies.

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Google Gemini API key.

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

5. Navigate to any project folder and run the application.

Example:

```bash
cd 04_AI_QA_Assistant
python app.py
```

---

# Repository Highlights

- Three complete AI applications built using LangChain and Google Gemini.
- Modular and reusable Python code.
- Comprehensive documentation covering prompt design, AI concepts, and project learnings.
- Clean Git commit history with meaningful commit messages.
- Structured repository for easy navigation and future enhancements.

---

# Author

**Antra Agarwal**

B.Tech Computer Science Engineering