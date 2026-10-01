import time

from google import genai

from app.config.settings import settings
from app.llm.provider import LLMProvider


class GeminiProvider(LLMProvider):

    # Tempo máximo total para uma tentativa de geração
    TIMEOUT_SECONDS = 10

    # Intervalo entre consultas do status da interaction
    POLL_INTERVAL_SECONDS = 1

    # Timeout máximo de cada chamada HTTP ao Gemini
    HTTP_TIMEOUT_SECONDS = 3

    # 1 chamada inicial + 1 retry
    MAX_ATTEMPTS = 2

    def __init__(self):
        if not settings.GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY não configurada"
            )

        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate(self, prompt: str) -> str:
        last_error = None

        for attempt in range(1, self.MAX_ATTEMPTS + 1):

            print(
                f"[Gemini] Tentativa "
                f"{attempt}/{self.MAX_ATTEMPTS}"
            )

            try:
                return self._generate_once(prompt)

            except TimeoutError as error:
                last_error = error

                print(
                    f"[Gemini] Tentativa {attempt} "
                    f"terminou por timeout: {error}"
                )

        raise RuntimeError(
            f"Gemini falhou após "
            f"{self.MAX_ATTEMPTS} tentativas"
        ) from last_error

    def _generate_once(self, prompt: str) -> str:
        start = time.perf_counter()

        # Cria a interaction em background para não bloquear
        interaction = self.client.interactions.create(
            model=settings.GEMINI_MODEL,
            input=prompt,
            background=True,
            timeout=self.HTTP_TIMEOUT_SECONDS
        )

        interaction_id = interaction.id

        print(
            f"[Gemini] Interaction iniciada: "
            f"{interaction_id}"
        )

        while True:

            # Consulta o status da interaction.
            # Esta chamada também possui timeout próprio.
            interaction = self.client.interactions.get(
                id=interaction_id,
                timeout=self.HTTP_TIMEOUT_SECONDS
            )

            elapsed = time.perf_counter() - start

            print(
                f"[Gemini] status={interaction.status} "
                f"tempo={elapsed:.2f}s"
            )

            # Resposta concluída
            if interaction.status == "completed":

                print(
                    f"[Gemini] respondeu em "
                    f"{elapsed:.2f}s"
                )

                return interaction.output_text

            # Gemini terminou com erro ou cancelamento
            if interaction.status in (
                "failed",
                "cancelled"
            ):
                raise RuntimeError(
                    f"Gemini finalizou com status: "
                    f"{interaction.status}"
                )

            # Tempo total da geração excedido
            if elapsed >= self.TIMEOUT_SECONDS:

                print(
                    f"[Gemini] Timeout de "
                    f"{self.TIMEOUT_SECONDS}s. "
                    "Cancelando interaction..."
                )

                try:
                    self.client.interactions.cancel(
                        id=interaction_id,
                        timeout=self.HTTP_TIMEOUT_SECONDS
                    )

                    print(
                        "[Gemini] Cancelamento solicitado"
                    )

                except Exception as cancel_error:
                    # Falha ao cancelar não deve impedir
                    # o timeout original de continuar.
                    print(
                        "[Gemini] Erro ao solicitar "
                        f"cancelamento: {cancel_error}"
                    )

                raise TimeoutError(
                    f"Gemini excedeu o timeout de "
                    f"{self.TIMEOUT_SECONDS} segundos"
                )

            time.sleep(
                self.POLL_INTERVAL_SECONDS
            )