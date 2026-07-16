from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Create the Gemini client
client = genai.Client(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Generate content
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Artificial Intelligence in simple words."
)

print(response.text)