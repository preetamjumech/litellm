import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

# Retrieve the Google API key from the environment
api_key = os.getenv('GOOGLE_API_KEY')

# Configure the genai client with your API key
genai.configure(api_key=api_key)

# Create the model object
model = genai.GenerativeModel('gemini-2.0-flash')

# Generate content
response = model.generate_content("How does AI work?")
print(response.text)