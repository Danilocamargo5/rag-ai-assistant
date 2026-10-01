from app.config.settings import settings
from app.llm.provider import LLMProvider
from app.llm.gemini_client import GeminiProvider
from app.llm.openai_client import OpenAIProvider


def create_llm_providers() -> list[LLMProvider]:
    providers = []

    for provider_name in settings.LLM_PROVIDERS:

        if provider_name == "gemini":
            providers.append(GeminiProvider())
            continue

        if provider_name == "openai":
            providers.append(OpenAIProvider())
            continue

        if provider_name == "bedrock":
            raise NotImplementedError(
                "BedrockProvider ainda não foi implementado"
            )

        raise ValueError(
            f"LLM provider não suportado: {provider_name}"
        )

    return providers