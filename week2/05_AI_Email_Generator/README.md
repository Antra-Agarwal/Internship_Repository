# AI Email Generator

## Overview

The AI Email Generator is a command-line Generative AI application built using **Python**, **LangChain**, and **Google Gemini**. It generates professional, well-structured emails based on user inputs such as email type, recipient, tone, purpose, and sender name.

The project demonstrates how prompt engineering and LangChain can be used to generate dynamic and context-aware content using Large Language Models (LLMs).

---

## Features

- Generate professional emails using AI
- Choose from common email types or enter a custom email type
- Select the desired writing tone
- Optional sender name for personalized signatures
- Automatically generates a subject line
- Save generated emails as `.txt` files
- Generate multiple versions of the same email
- Interactive command-line interface
- Secure API key management using `.env`
- User-friendly error handling

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
05_AI_Email_Generator/
│
├── app.py
└── README.md
```

---

## How It Works

1. The user selects or enters an email type.
2. The user provides the recipient.
3. The user selects the tone.
4. The user enters the purpose of the email.
5. The user can optionally provide a sender name.
6. LangChain inserts the inputs into a Prompt Template.
7. Gemini generates a professional email.
8. The generated email is displayed in the terminal.
9. The user can save the email as a text file or generate another version.

### Workflow

```
User Input
     │
     ▼
Email Details
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
Generated Email
     │
     ▼
Display / Save as Text File
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
```

### Navigate to the project folder

```bash
cd Internship/Week2/05_AI_Email_Generator
```

### Install dependencies

```bash
pip install -r ../requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root directory.

```text
GOOGLE_API_KEY=YOUR_API_KEY
```

---

## Running the Application

```bash
python app.py
```

---

## Sample Run

```
===========================================================================
📧 AI Email Generator
Powered by LangChain + Google Gemini
===========================================================================

Choose Email Type

1. Leave Application
2. Resignation
3. Thank You
4. Apology
5. Meeting Request
6. Job Application
7. Follow-up

Or type your own email type.

Enter choice or custom email type: 1

Recipient: Project Manager

Choose Tone

1. Professional
2. Formal
3. Friendly

Enter choice: 1

Purpose of the Email:
Request leave for two days due to illness.

Sender Name (Optional):
Antra

Generating email...

---------------------------------------------------------------------------
Subject: Leave Application for Two Days

Dear Project Manager,

I hope you are doing well.

I am writing to request a leave of absence for two days due to illness.
I would be grateful if you could kindly approve my leave request.

Thank you for your understanding.

Kind regards,

Antra
---------------------------------------------------------------------------
```

---

## Key Concepts Used

- Large Language Models (LLMs)
- Prompt Engineering
- Prompt Templates
- LangChain Chains
- Output Parsers
- Environment Variables
- File Handling
- Exception Handling

---

## Challenges Faced

- Designing reusable prompts
- Generating emails with different tones
- Handling API rate limits
- Managing user inputs efficiently
- Saving generated content to files

---

## Future Improvements

- Support additional writing tones
- Export emails as PDF or Word documents
- Email templates for different industries
- Web interface using Streamlit
- Email preview with formatting

---

## Learning Outcomes

After completing this project, I learned how to:

- Build AI-powered content generation applications.
- Use Prompt Templates to generate dynamic responses.
- Integrate LangChain with Google Gemini.
- Design modular Python applications.
- Handle user input and file operations.
- Improve user experience with menus and reusable functions.

---

## Author

**Antra Agarwal**

B.Tech Computer Science Engineering