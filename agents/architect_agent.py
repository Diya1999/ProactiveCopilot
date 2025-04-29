from langchain_community.llms import Ollama
# from langchain_ollama.llms import OllamaLLM
from loguru import logger
import warnings
warnings.filterwarnings("ignore")
import os
import subprocess

class ArchitectAgent:
    def __init__(self, model_name="llama3.2", temperature=0.3):
        self.llm = Ollama(model=model_name)
        #model=OllamaLLM(model="llama3.2")
        self.temperature = temperature

    def analyze_architecture(self, code: str) -> str:
        logger.info("🏛️ [ArchitectAgent] Analyzing software architecture...")

        prompt = f"""
            You are a senior software architect.

            Analyze the following Python code:
            ```python
            {code}
            Evaluate the code for the following aspects:

            Is the system modular and well-organized?

            Are there any architectural anti-patterns (tight coupling, poor layering, etc.)?

            Is this code easily scalable and maintainable?

            Suggest improvements to make the system more robust, modular, or scalable.

            Respond with a structured report under headings:

            Architecture Issues

            Scalability Concerns

            Maintainability Feedback

            Suggestions for Improvement """

        response = self.llm.invoke(prompt)
        return response.strip()