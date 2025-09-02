# AI-AgentsChatbot-Learning-Portfolio

## Overview
Learning project to build a personal AI assistant integrating chatbots, AI agents, DevOps, and AWS. Built step by step as a junior developer, starting with a basic chatbot in Python and Streamlit. Goal: End-to-end deployment in the cloud.

## Phase 1: Assistant Foundation (Completed)
- **Description**: Local chatbot that responds to questions with basic memory, using a local LLM (TinyLlama) to avoid costs.
- **Tech Stack**: Python 3.12, Streamlit for UI, llama-cpp-python for LLM (no Docker to save space).
- **How to Run Locally**:
  1. Clone the repo: `git clone https://github.com/LuisPenafiel/AI-AgentsChatbot-Learning-Portfolio.git`
  2. Create venv: `python -m venv venv; source venv/bin/activate`
  3. Install dependencies: `pip install -r requirements.txt`
  4. Run the chatbot: `streamlit run app.py`
  5. Open the link in your browser and test prompts.

## Roadmap (Simplified for Juniors)
- Phase 1: Basic chatbot (done).
- Phase 2: Add agents (autonomy with tools like web search).
- Phase 3: Basic DevOps (GitHub Actions, optional Docker).
- Phase 4: Cloud deployment on AWS (free tier).
- Tips: Start small, test locally first, use print() for debugging. If space is low in Codespaces, avoid heavy packages.

## Installation and Debug
- Requirements: Python 3.12+, Git.
- Common issues: Space in Codespaces (~32GB limit), package versions (use fixed in requirements.txt).
- For debug: `pip list | grep langchain` or `df -h` for space.

## Contributions
Fork and PR if you want to improve. For juniors, start with simple projects and build up!

## License
MIT – Free to use.