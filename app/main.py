from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.llm.factory import create_llm_providers
from app.llm.service import LLMService
from app.llm.exceptions import LLMUnavailableError


app = FastAPI()

llm_providers = create_llm_providers()
llm_service = LLMService(llm_providers)


class QuestionRequest(BaseModel):
    question: str


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


@app.post("/questions")
def ask_question(request: QuestionRequest):

    try:
        answer = llm_service.generate(
            request.question
        )

        return {
            "question": request.question,
            "answer": answer
        }

    except LLMUnavailableError as error:

        raise HTTPException(
            status_code=503,
            detail=str(error)
        ) from error