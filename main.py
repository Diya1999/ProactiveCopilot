from agents.orchestrator import Orchestrator
from loguru import logger

def main():
    logger.info("Starting Proactive Copilot Multi-Agent System")

    # Initialize the Orchestrator
    orchestrator = Orchestrator()

    # Kick off a sample task
    sample_task = "Write a FastAPI endpoint for user authentication"
    orchestrator.start_project(sample_task)

if __name__ == "__main__":
    main()
