import unittest
from unittest.mock import Mock

from app.llm.service import LLMService
from app.llm.exceptions import LLMUnavailableError


class TestLLMService(unittest.TestCase):

    def test_first_provider_success(self):
        gemini = Mock()
        gemini.generate.return_value = "Resposta Gemini"

        openai = Mock()

        service = LLMService([gemini, openai])
        result = service.generate("O que é RAG?")

        self.assertEqual(result, "Resposta Gemini")
        gemini.generate.assert_called_once_with("O que é RAG?")
        openai.generate.assert_not_called()

    def test_fallback_to_second_provider(self):
        gemini = Mock()
        gemini.generate.side_effect = RuntimeError("Gemini falhou")

        openai = Mock()
        openai.generate.return_value = "Resposta OpenAI"

        service = LLMService([gemini, openai])
        result = service.generate("O que é RAG?")

        self.assertEqual(result, "Resposta OpenAI")
        gemini.generate.assert_called_once()
        openai.generate.assert_called_once()

    def test_all_providers_fail(self):
        gemini = Mock()
        gemini.generate.side_effect = RuntimeError("Gemini falhou")

        openai = Mock()
        openai.generate.side_effect = RuntimeError("OpenAI falhou")

        service = LLMService([gemini, openai])

        with self.assertRaises(LLMUnavailableError):
            service.generate("O que é RAG?")

        gemini.generate.assert_called_once()
        openai.generate.assert_called_once()

    def test_empty_provider_list(self):
        with self.assertRaises(ValueError):
            LLMService([])


if __name__ == "__main__":
    unittest.main()