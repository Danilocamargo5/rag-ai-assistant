import time
from openai import OpenAI

from app.config.settings import settings
from app.llm.provider import LLMProvider


class OpenAIProvider(LLMProvider):

    def __init__(self):
        if not settings.OPENAI_API_KEY:
            raise ValueError(
                "OPENAI_API_KEY não configurada"
            )

        self.client = OpenAI(
            api_key=settings.OPENAI_API_KEY
        )

    def generate(self, prompt: str) -> str:
        start = time.perf_counter()

        response = self.client.responses.create(
            model=settings.OPENAI_MODEL,
            input=prompt
        )

        elapsed = time.perf_counter() - start

        print(f"OpenAI respondeu em {elapsed:.2f} segundos")

        return response.output_text