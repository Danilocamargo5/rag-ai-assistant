import os

from google import genai

from app.llm.provider import LLMProvider


class GeminiProvider(LLMProvider):

    def __init__(self):
        api_key = os.getenv("GEMINI_API_KEY")
        self.client = genai.Client(api_key=api_key)

    def generate(self, prompt: str) -> str:
        interaction = self.client.interactions.create(
            model="gemini-3.8-flash",
            input=prompt
        )

        return interaction.output_text