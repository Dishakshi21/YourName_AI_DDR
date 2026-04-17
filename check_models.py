import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("Available Models:\n")

for model in genai.list_models():
    print(model.name, " | Supported:", model.supported_generation_methods)