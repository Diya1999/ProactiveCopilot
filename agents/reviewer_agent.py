
from langchain_community.llms import Ollama
# from langchain_ollama.llms import OllamaLLM
from loguru import logger
import os
import subprocess
import warnings
warnings.filterwarnings("ignore")

class ReviewerAgent:
    def __init__(self, model_name="llama3.2", temperature=0.3):
        self.llm = Ollama(model=model_name)
        self.temperature = temperature

    def review_code(self, code: str) -> str:
        logger.info("🔎 [ReviewerAgent] Reviewing generated code...")
        # Save the generated code temporarily
        filename = "temp_code.py"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)
        pylint_report = self.run_pylint(filename)
        flake8_report = self.run_flake8(filename)
        llm_feedback = self.llm.invoke(
            f"""
                You are a senior software engineer reviewing code.

                Here is the code:
                ```python
                {code}
                Please answer:

                Are there any obvious bugs, bad practices, or missing validations?

                Are there performance issues or security risks?

                Suggest improvements.

                Respond clearly with sections: Bugs / Risks / Suggestions. """ )
        os.remove(filename)        
        review_report = (
        "==== Static Analysis ====\n\n"
        f"Pylint Report:\n{pylint_report}\n\n"
        f"Flake8 Report:\n{flake8_report}\n\n"
        "==== LLM High-Level Feedback ====\n\n"
        f"{llm_feedback}"
                        )
        return review_report

    def run_pylint(self, filename: str) -> str:
        """Run pylint on the code file."""
        try:
            output = subprocess.check_output(
                ["pylint", filename, "--disable=all", "--enable=errors,warnings"],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
        except subprocess.CalledProcessError as e:
            output = e.output
        return output.strip()

    def run_flake8(self, filename: str) -> str:
        """Run flake8 on the code file."""
        try:
            output = subprocess.check_output(
                ["flake8", filename],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
        except subprocess.CalledProcessError as e:
            output = e.output
        return output.strip()
