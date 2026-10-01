import time
from google import genai

from app.config.settings import settings
from app.llm.provider import LLMProvider


class GeminiProvider(LLMProvider):

    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY não configurada")

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:
        start = time.perf_counter()

        interaction = self.client.interactions.create(
            model=settings.GEMINI_MODEL,
            input=prompt
        )

        elapsed = time.perf_counter() - start

        print(f"Gemini respondeu em {elapsed:.2f} segundos")

        return interaction.output_text