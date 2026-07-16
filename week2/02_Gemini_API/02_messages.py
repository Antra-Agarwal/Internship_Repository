from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()

client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

response = client.models.generate_content(
    model="gemini-2.5-flash",

    config=types.GenerateContentConfig(
        system_instruction="You are a friendly Python teacher. Explain everything in simple language."
    ),

    contents="What is Object-Oriented Programming?"
)

print(response.text)