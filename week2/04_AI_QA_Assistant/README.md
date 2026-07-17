# AI Question Answering Assistant

## Overview

The AI Question Answering Assistant is a command-line GenAI application built using **Python**, **LangChain**, and **Google Gemini**. It allows users to ask questions on any topic and receive AI-generated answers in natural language.

The project demonstrates how Large Language Models (LLMs) can be integrated into Python applications using LangChain pipelines.

---

## Features

- Answer questions on any topic
- Interactive command-line interface
- Uses Google's Gemini LLM
- Reusable Prompt Template
- LangChain pipeline implementation
- User-friendly error handling
- Secure API key management using `.env`
- Multiple exit commands (`exit`, `quit`, `bye`)

---

## Technologies Used

- Python 3
- Google Gemini API
- LangChain
- langchain-google-genai
- python-dotenv

---

## Project Structure

```
04_AI_QA_Assistant/
│
├── app.py
└── README.md
```

---

## How It Works

1. The user enters a question.
2. The question is inserted into a Prompt Template.
3. LangChain sends the prompt to the Gemini model.
4. Gemini generates an answer.
5. The response is converted into plain text.
6. The answer is displayed in the terminal.

### Workflow

```
User
   │
   ▼
Question
   │
   ▼
Prompt Template
   │
   ▼
LangChain
   │
   ▼
Google Gemini
   │
   ▼
Output Parser
   │
   ▼
Terminal
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project

```bash
cd Internship/Week2/04_AI_QA_Assistant
```

### Install dependencies

```bash
pip install -r ../requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory of the project.

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Running the Application

```bash
python app.py
```

---

## Sample Output

```
======================================================================
🤖 AI Question Answering Assistant
Powered by LangChain + Google Gemini
======================================================================

Ask your question:
What is Artificial Intelligence?

Generating answer...

----------------------------------------------------------------------
Artificial Intelligence (AI) is a field of computer science that enables
machines to perform tasks that typically require human intelligence,
such as learning, reasoning, and decision-making.

Example:
Virtual assistants like Google Assistant and Siri use AI to understand
and respond to user queries.
----------------------------------------------------------------------

Ask your question:
exit

Thank you for using the AI Question Answering Assistant!
```

---

## Key Concepts Used

- Large Language Models (LLMs)
- Prompt Engineering
- Prompt Templates
- LangChain Chains
- Output Parsers
- Environment Variables
- Exception Handling

---

## Challenges Faced

- Understanding LangChain pipelines
- Configuring the Gemini API
- Managing API rate limits
- Designing reusable prompts

---

## Future Improvements

- Conversation history
- Voice input support
- Streamlit web interface
- Chat history storage
- Support for multiple LLM providers

---

## Learning Outcomes

After completing this project, I learned how to:

- Integrate Gemini into a Python application.
- Build AI applications using LangChain.
- Design reusable prompts.
- Create modular and maintainable Python code.
- Handle API errors gracefully.
- Secure API keys using environment variables.

---

## Author

**Antra Agarwal**

B.Tech Computer Science Engineering