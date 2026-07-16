from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# Load environment variables
load_dotenv()

# Create the chat model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0.3,
)

# Send a message
response = llm.invoke(
    [HumanMessage(content="Explain Artificial Intelligence in simple words.")]
)

# Print the response
print(response.content)