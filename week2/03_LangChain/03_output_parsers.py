from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

# Prompt Template
prompt = PromptTemplate.from_template(
    "Explain {topic} in one short paragraph."
)

# Output Parser
parser = StrOutputParser()

# Create a chain
chain = prompt | llm | parser

# Run the chain
response = chain.invoke(
    {"topic": "Artificial Intelligence"}
)

print(response)