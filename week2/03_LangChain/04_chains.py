from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load API Key
load_dotenv()

# Create Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

# Create Prompt Template
prompt = PromptTemplate.from_template(
    """
You are a helpful AI tutor.

Explain the following topic:

{topic}

Use:
- Simple language
- One example
- Maximum 200 words
"""
)

# Output Parser
parser = StrOutputParser()

# Create Chain
chain = prompt | llm | parser

# User Input
topic = input("Enter a topic: ")

# Run Chain
response = chain.invoke(
    {
        "topic": topic
    }
)

print("\nGenerated Response:\n")
print(response)