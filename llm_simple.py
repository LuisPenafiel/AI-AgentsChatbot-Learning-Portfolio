from langchain_community.llms import LlamaCpp
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun

# Load the model with LangChain wrapper
llm = LlamaCpp(
    model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=1,
    temperature=0.7,
    max_tokens=500,
    verbose=True  # For debug
)

# Tool for web search
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for searching current info on the web. Input: search query."
    ),
]

# Initialize agent
agent = initialize_agent(
    tools, llm, agent_type="zero-shot-react-description", verbose=True
)

# Test
prompt = "Search and summarize 3 tips to learn AI as a junior."
response = agent.run(prompt)
print("Agent Response:", response)