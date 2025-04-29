# Proactive Copilot: A Multi-Agent AI System for Autonomous Code Improvement

---

## 📚 Project Overview

**Proactive Copilot** is a fully autonomous **multi-agent AI system** designed to proactively assist in software development by **generating**, **reviewing**, **fixing**, **testing**, and **architecturally analyzing** code without human intervention at every stage.

Unlike passive code suggestion tools, **Proactive Copilot** mimics a **real software engineering team** through agent collaboration: iteratively refining code until it reaches production-grade quality.

---

## 🧠 Multi-Agent Team

| Agent | Role |
|:---|:---|
| **CodeWriterAgent** | Generates Python code based on task description. |
| **ReviewerAgent** | Performs static code analysis (Pylint, Flake8) and AI-driven quality review. |
| **CodeFixerAgent** | Refines and corrects code based on reviewer and testing feedback. |
| **TesterAgent** | Auto-generates Pytest-based unit tests and validates code behavior. |
| **ArchitectAgent** | Evaluates system architecture, modularity, scalability, and maintainability. |
| **Orchestrator** | Coordinates the multi-agent workflow with iteration and healing loops. |

---

## 🔁 Intelligent Workflow Loop

```plaintext
1. CodeWriterAgent generates initial code.
2. ReviewerAgent analyzes the code.
3. If issues detected → CodeFixerAgent patches code.
4. Re-review the fixed code.
5. When Reviewer passes code → TesterAgent generates & runs unit tests.
6. If tests fail → CodeFixerAgent refines the code again.
7. Repeat until both code review and tests pass, or after 3 maximum attempts.
8. ArchitectAgent performs final architectural risk evaluation.
9. Final high-quality code delivered ✅
