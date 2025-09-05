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

## Phase 2: Adding Autonomy with Agents (Completed)

- **Description**: Enhanced the chatbot with AI agents for autonomy, allowing tasks like web search and summarization. Agents use tools to "think" and act on complex queries.
- **Tech Stack**: Added LangChain for agents and tools, DuckDuckGo for web search.
- **How to Run Locally**:

 1.Run python llm_simple.py for a console test (searches and summarizes).
 2.In app.py, the chatbot now uses agents – test with prompts like "Search and summarize AI tips for juniors."
 Notes: Agents show "thinking" steps in the terminal (verbose=True for debugging). Simple and extensible for more tools.


## Phase 3: Basic DevOps (Completed)

- Git branches for features.
- CI with GitHub Actions for auto-tests.
- How to test: Push to main, check Actions tab.

## Phase 4: Automation and Monitoring (Completed)
- **Description:** Added workflow automation with n8n (low-code flows for chatbot integration) and monitoring with Grafana (dashboards for metrics/logs, e.g., response time, CPU).
- **Tech Stack:** n8n for workflows, Grafana for observability.
- **How to Run Locally:**
  1. Install n8n: `npm install -g n8n` (need Node.js: `sudo apt install nodejs npm`).
  2. Start n8n: `n8n start` (browser: http://localhost:5678).
  3. Install Grafana: Download binary from grafana.com, run `./bin/grafana-server` (browser: http://localhost:3000).
  4. Example workflow in n8n: Monitor app.py logs, send email alert if error.
- **Notes:** n8n integrates chatbot with external services (e.g., notifications), Grafana shows performance. Local to avoid costs/cloud.

## Roadmap 
- Phase 1: Basic chatbot (done).
- Phase 2: Add agents (autonomy with tools like web search).
- Phase 3: Basic DevOps (GitHub Actions, optional Docker).
- Phase 4: n8n for workflows, Grafana for observability
- Tips: Start small, test locally first, use print() for debugging. If space is low in Codespaces, avoid heavy packages.

## Installation and Debug
- Requirements: Python 3.12+, Git.
- Common issues: Space in Codespaces (~32GB limit), package versions (use fixed in requirements.txt).
- For debug: `pip list | grep langchain` or `df -h` for space.

## Contributions
Fork and PR if you want to improve. For juniors, start with simple projects and build up!

## License
MIT – Free to use.