import os

from dotenv import load_dotenv


load_dotenv()


class Settings:
    LLM_PROVIDERS = [
        provider.strip().lower()
        for provider in os.getenv(
            "LLM_PROVIDERS",
            "gemini"
        ).split(",")
    ]

    # Gemini
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv(
        "GEMINI_MODEL",
        "gemini-3.8-flash"
    )

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv(
        "OPENAI_MODEL",
        "gpt-5.6-luna"
    )

    # AWS Bedrock
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    BEDROCK_MODEL = os.getenv("BEDROCK_MODEL")


settings = Settings()