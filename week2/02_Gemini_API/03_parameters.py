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

    contents="Write a short motivational message for students.",

    config=types.GenerateContentConfig(
        temperature=0.8,
        max_output_tokens=100,
        top_p=0.95,
        top_k=40,
    )
)

print(response.text)