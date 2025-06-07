from litellm import completion
import os
import json
from dotenv import load_dotenv

load_dotenv()
os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY")  # Load environment variables from .env file
os.environ['GROQ_API_KEY'] = os.getenv("GROQ_API_KEY")


response1 = completion(
    model="gemini/gemini-2.5-flash-preview-04-17", 
    messages=[{"role": "user", "content": "tell me a one line joke about AI"}],
)
response_dict = response1.model_dump()
print(json.dumps(response_dict, indent=2, ensure_ascii=False))


response2 = completion(
    model="groq/meta-llama/llama-4-scout-17b-16e-instruct", 
    messages=[{"role": "user", "content": "tell me a one line joke about AI"}],
)
response_dict = response2.model_dump()
print(json.dumps(response_dict, indent=2, ensure_ascii=False))