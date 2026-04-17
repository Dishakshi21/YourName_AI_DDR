import google.generativeai as genai
import os
import json
from utils.prompts import PARSER_PROMPT
from dotenv import load_dotenv

# load env
load_dotenv()

# configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ DEFINE MODEL (THIS WAS MISSING)
model = genai.GenerativeModel("gemini-flash-latest")


def parse_text(text):
    response = model.generate_content(
        PARSER_PROMPT + "\n\n" + text,
        generation_config={"temperature": 0}
    )

    raw_output = response.text.strip()

    try:
        # remove ```json ``` if present
        if raw_output.startswith("```"):
            raw_output = raw_output.replace("```json", "").replace("```", "").strip()

        parsed = json.loads(raw_output)

        if isinstance(parsed, dict):
            parsed = [parsed]

        return parsed

    except Exception as e:
        print("Parsing Error:", e)
        print("Raw Output:", raw_output)

        return [{
            "area": "Not Available",
            "issue": "Not Available",
            "observation": raw_output,
            "severity": "Not Available",
            "temperature": "Not Available"
        }]