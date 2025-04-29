from langchain_community.llms import Ollama
# from langchain_ollama.llms import OllamaLLM
from loguru import logger
import warnings
warnings.filterwarnings("ignore")

class CodeWriterAgent:
    def __init__(self, model_name="llama3.2", temperature=0.3):
        self.llm = Ollama(model=model_name)
        #model=OllamaLLM(model="llama3.2")
        self.temperature = temperature

    def _extract_code(self, llm_output: str) -> str:
        """
        Simple method to extract ```python code``` block.
        """
        if "```python" in llm_output:
            code = llm_output.split("```python")[1].split("```")[0].strip()
            return code
        else:
            return llm_output.strip()

    def generate_code(self, task_description: str) -> str:
        logger.info("🧠 [CodeWriterAgent] Generating code for task...")
        prompt = f"""
            You are an expert software engineer.
            Your task is: {task_description}

            Write clean, modular, production-quality Python code.
            Add docstrings, error handling, and follow best practices.
            Respond ONLY with the code inside triple backticks ```python ... ```
            Do not add any extra explanations.
                    """
        response = self.llm(prompt)
        code=self._extract_code(response)
        return code 