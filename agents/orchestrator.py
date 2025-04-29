from agents.code_writer_agent import CodeWriterAgent
from agents.reviewer_agent import ReviewerAgent
from agents.tester_agent import TesterAgent
from agents.architect_agent import ArchitectAgent
import loguru as logger

class Orchestrator:
    def __init__(self):
        self.writer = CodeWriterAgent()
        self.reviewer = ReviewerAgent()
        self.tester = TesterAgent()
        self.architect = ArchitectAgent()

    def start_project(self, task):
        logger.info(f"🚀 Starting Proactive Copilot System for task: {task}")

        code = self.writer.generate_code(task)
        max_attempts = 3
        attempt = 0

        while attempt < max_attempts:
            print(f"\n🔁 Iteration {attempt + 1}")

            # Review the code
            review = self.reviewer.review_code(code)

            review_passed = (
                "no major issues" in review.lower()
                or "no bugs" in review.lower()
                or "clean" in review.lower()
            )

            if review_passed:
                print("✅ Review passed! Now running tests...")
                # Test the code
                tests_result = self.tester.generate_tests(code)

                if "failed" not in tests_result.lower() and "error" not in tests_result.lower():
                    print("🎯 Tests passed! Code is ready! ✅")
                    break
                else:
                    print("⚡ Tests failed. Attempting to fix based on test errors...")
                    code = self.fixer.fix_code(code, tests_result)
            else:
                print("⚡ Review failed. Attempting to fix based on reviewer feedback...")
                code = self.fixer.fix_code(code, review)

            attempt += 1

        # Architecture analysis after fixing
        risks = self.architect.analyze_architecture(code)

        print("\n--- Final Results ---")
        print(f"🧩 Final Code:\n{code}")
        print(f"🛡️ Review Feedback:\n{review}")
        print(f"🏛️ Architecture Insights:\n{risks}")