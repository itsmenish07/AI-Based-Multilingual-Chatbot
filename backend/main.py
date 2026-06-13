from fastapi import FastAPI
from pydantic import BaseModel

from eligibility import check_eligibility
from chatbot import ask_question

app = FastAPI()


class UserInput(BaseModel):
    age: int
    gender: str
    occupation: str
    income: int
    state: str
    category: str
    area: str


class ChatRequest(BaseModel):
    question: str
    language: str = "English"


@app.get("/")
def home():
    return {
        "message": "Welfare Scheme Assistant Running"
    }


@app.post("/check-eligibility")
def eligibility(data: UserInput):

    results = check_eligibility(data.dict())

    return {
        "eligible_schemes": results
    }


@app.post("/chat")
def chat(data: ChatRequest):

    answer = ask_question(
        data.question,
        data.language
    )

    return {
        "answer": answer
    }