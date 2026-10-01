from app.llm.provider import LLMProvider


class LLMService:

    def __init__(self, providers: list[LLMProvider]):
        if not providers:
            raise ValueError("Nenhum LLM provider configurado")

        self.providers = providers

    def generate(self, prompt: str) -> str:

        last_error = None

        for provider in self.providers:
            try:
                return provider.generate(prompt)

            except Exception as error:
                last_error = error

        raise RuntimeError(
            "Todos os LLM providers falharam"
        ) from last_error