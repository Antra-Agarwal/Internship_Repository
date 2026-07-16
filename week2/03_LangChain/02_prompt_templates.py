from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Load API key
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

# Create a Prompt Template
prompt = PromptTemplate.from_template(
    "Explain {topic} in simple language with an example."
)

# Fill the placeholder
formatted_prompt = prompt.format(topic="Machine Learning")

print("Generated Prompt:\n")
print(formatted_prompt)

print("\n" + "=" * 50 + "\n")

# Send to Gemini
response = llm.invoke(formatted_prompt)

print(response.content)