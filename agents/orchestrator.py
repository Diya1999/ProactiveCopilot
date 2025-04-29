from agents.code_writer_agent import CodeWriterAgent
from agents.reviewer_agent import ReviewerAgent
from agents.tester_agent import TesterAgent
from agents.architect_agent import ArchitectAgent

class Orchestrator:
    def __init__(self):
        self.writer = CodeWriterAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()
        self.architect = ArchitectAgent()

    def start_project(self, task):
        print(f"\n🚀 Project Task: {task}")

        code = self.writer.generate_code(task)
        review = self.reviewer.review_code(code)
        tests = self.tester.generate_tests(code)
        risks = self.architect.analyze_architecture(code)

        print("\n--- Final Results ---")
        print(f"Generated Code:\n{code}")
        print(f"Review Feedback:\n{review}")
        print(f"Generated Tests:\n{tests}")
        print(f"Architecture Insights:\n{risks}")