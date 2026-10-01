from fastapi import FastAPI
from pydantic import BaseModel

from app.llm.factory import create_llm_providers
from app.llm.service import LLMService


app = FastAPI()

llm_providers = create_llm_providers()
llm_service = LLMService(llm_providers)


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/questions")
def ask_question(request: QuestionRequest):
    answer = llm_service.generate(request.question)

    return {
        "question": request.question,
        "answer": answer
    }