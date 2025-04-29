from langchain_community.llms import Ollama
# from langchain_ollama.llms import OllamaLLM
from loguru import logger
import warnings
warnings.filterwarnings("ignore")
import os
import subprocess
class TesterAgent:
    def __init__(self, model_name="llama3.2", temperature=0.3):
        self.llm = Ollama(model=model_name)
        self.temperature = temperature
    def generate_tests(self, code: str) -> str:
        logger.info("🧪 [TesterAgent] Generating and running unit tests...")

        # Save the code into a temporary file
        code_filename = "temp_code.py"
        with open(code_filename, "w", encoding="utf-8") as f:
            f.write(code)

        # 1. Generate Unit Tests using LLM
        prompt = f"""
        You are an expert QA engineer.

        Please write pytest-based unit tests for the following Python code:
        ```python
        {code}
        Focus on important functions like authentication, token generation, token validation.

        Write at least 3 test cases.

        DO NOT import "your_app" or assume any app module. Assume all code is available locally.

        Use direct function calls or API simulation if needed.

        Only output the test code inside triple backticks.

        No explanations, only valid test code. """

        llm_response = self.llm.invoke(prompt)
        tests = self._extract_code(llm_response)

        # Save the generated tests into a file
        test_filename = "test_temp_code.py"
        with open(test_filename, "w", encoding="utf-8") as f:
            f.write(tests)

        # 2. Run pytest on generated tests
        pytest_output = self.run_pytest(test_filename)

        # Clean up temp files
        os.remove(code_filename)
        os.remove(test_filename)

        return pytest_output

    def _extract_code(self, llm_output: str) -> str:
        """
        Extracts code between ```python ... ``` tags from LLM output.
        """
        if "```python" in llm_output:
            return llm_output.split("```python")[1].split("```")[0].strip()
        else:
            return llm_output.strip()


    def run_pytest(self, test_filename: str) -> str:
        """
        Run pytest on the generated test file and capture the output.
        """
        try:
            output = subprocess.check_output(
                ["pytest", test_filename, "-v"],
                stderr=subprocess.STDOUT,
                universal_newlines=True
            )
        except subprocess.CalledProcessError as e:
            output = e.output
        return output.strip()