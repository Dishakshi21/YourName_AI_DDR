# AI DDR Generator

## Overview
This project converts inspection and thermal reports into a structured DDR (Detailed Diagnostic Report).

## Features
- Extracts text & images from PDFs
- Combines multiple reports
- Handles missing/conflicting data
- Generates structured client-ready report

## Tech Stack
- Python
- Streamlit
- Gemini API
- PyMuPDF

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Add API key in `.env`

3. Run:
   streamlit run app.py
