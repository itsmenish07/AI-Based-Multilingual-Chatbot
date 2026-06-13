import os

from dotenv import load_dotenv
import google.generativeai as genai

from rag.retriever import retrieve
from translator import (
    translate_to_english,
    translate_to_hindi,
    translate_to_tamil
)

# Load environment variables
load_dotenv()

# Configure Gemini
genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def ask_question(
    question,
    language="English"
):

    original_question = question

    if language == "Hindi":
        question = translate_to_english(
            question
        )

    context = retrieve(question)

    prompt = f"""
Context:
{context}

Question:
{question}
"""

    response = model.generate_content(
        prompt
    )

    answer = response.text

    if language == "Hindi":
        answer = translate_to_hindi(
            answer
        )
    elif language == "Tamil":
        answer = translate_to_tamil(answer)

    return answer