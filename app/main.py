import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from app.llm.factory import create_llm_provider

load_dotenv()

llm_provider = create_llm_provider()

gemini_api_key = os.getenv("GEMINI_API_KEY")


app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/questions")
def ask_question(request: QuestionRequest):
    answer = llm_provider.generate(request.question)

    return {
        "question": request.question,
        "answer": answer
    }