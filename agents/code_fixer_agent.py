from langchain_community.llms import Ollama
# from langchain_ollama.llms import OllamaLLM
from loguru import logger
import warnings
warnings.filterwarnings("ignore")
import os
import subprocess

class CodeFixerAgent:
    def __init__(self, model_name="llama3.2", temperature=0.3):
        self.llm = Ollama(model=model_name)
        #model=OllamaLLM(model="llama3.2")
        self.temperature = temperature
    def fix_code(self, original_code: str, review_feedback: str) -> str:
        logger.info("🛠️ [CodeFixerAgent] Attempting to fix code based on review feedback...")

        prompt = f"""
        You are an expert Python developer.

        You are given:
        - Code:
        ```python
        {original_code}
        Review Feedback: {review_feedback}

        Please:

        Improve the code based on the feedback.

        Fix bugs, add missing validation, follow style suggestions.

        DO NOT rewrite from scratch — only improve the existing code.

        Output ONLY the improved Python code inside triple backticks.

        Make the code ready for production quality. """

        response = self.llm.invoke(prompt)
        improved_code = self._extract_code(response)
        return improved_code

    def _extract_code(self, llm_output: str) -> str:
        if "```python" in llm_output:
            return llm_output.split("```python")[1].split("```")[0].strip()
        else:
            return llm_output.strip()