from app.llm.provider import LLMProvider
from app.llm.exceptions import LLMUnavailableError


class LLMService:

    def __init__(self, providers: list[LLMProvider]):
        if not providers:
            raise ValueError(
                "Nenhum LLM provider configurado"
            )

        self.providers = providers

    def generate(self, prompt: str) -> str:
        last_error = None

        for provider in self.providers:

            provider_name = provider.__class__.__name__

            print(
                f"[LLMService] Tentando provider: "
                f"{provider_name}"
            )

            try:
                response = provider.generate(prompt)

                print(
                    f"[LLMService] Provider "
                    f"{provider_name} respondeu com sucesso"
                )

                return response

            except Exception as error:
                last_error = error

                print(
                    f"[LLMService] Provider "
                    f"{provider_name} falhou"
                )

                print(
                    f"[LLMService] Tipo do erro: "
                    f"{type(error).__name__}"
                )

                print(
                    f"[LLMService] Erro: {error}"
                )

                print(
                    "[LLMService] Tentando próximo "
                    "provider..."
                )

        raise LLMUnavailableError(
            "Nenhum LLM provider está disponível no momento"
        ) from last_error