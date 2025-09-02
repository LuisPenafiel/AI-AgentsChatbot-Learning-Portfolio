import streamlit as st
from langchain_community.llms import LlamaCpp
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun

# Load the model with LangChain wrapper
llm = LlamaCpp(
    model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=1,
    temperature=0.7,
    max_tokens=500,
    verbose=True  # For debug in terminal
)

# Memory for conversation
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Tool for web search
search = DuckDuckGoSearchRun()

tools = [
    Tool(
        name="Web Search",
        func=search.run,
        description="Useful for searching current info on the web. Input: search query."
    ),
]

# Initialize agent with memory
agent = initialize_agent(
    tools, llm, agent_type="chat-conversational-react-description", memory=st.session_state.memory, verbose=True
)

st.title("AI Assistant with Agents")

# Show conversation history
for message in st.session_state.memory.chat_memory.messages:
    st.write(f"{message.type.capitalize()}: {message.content}")

# User input
user_input = st.text_input("Enter your message:")
if st.button("Send"):
    if user_input:
        response = agent.run(user_input)
        st.write("Assistant:", response)