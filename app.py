import streamlit as st
from llama_cpp import Llama

# Load the model
llm = Llama(model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", n_ctx=2048, n_threads=1)

st.title("Basic AI Assistant")

# User input
user_input = st.text_input("Enter your message:")
if st.button("Send"):
    if user_input:
        response = llm(user_input, max_tokens=500, temperature=0.7)
        st.write("Assistant:", response["choices"][0]["text"])