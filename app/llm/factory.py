import os

from app.llm.provider import LLMProvider
from app.llm.gemini_client import GeminiProvider


def create_llm_provider() -> LLMProvider:
    provider = os.getenv("LLM_PROVIDER", "gemini")

    if provider == "gemini":
        return GeminiProvider()

    raise ValueError(f"LLM provider não suportado: {provider}")