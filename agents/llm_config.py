import os
from dotenv import load_dotenv

load_dotenv()

llm_config = {
    "model": "gpt-4o-mini",   # change if needed
    "api_key": os.getenv("OPENAI_API_KEY"),
    "temperature": 0.2,
}
