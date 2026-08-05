import os

from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ==========================
# API Keys
# ==========================

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if GOOGLE_API_KEY is None:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please add it to your .env file."
    )

# ==========================
# Models
# ==========================

LLM_MODEL = "gemini-3.6-flash"

EMBEDDING_MODEL = "gemini-embedding-001"