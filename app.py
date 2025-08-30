import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Memoria para contexto
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

chain = ConversationChain(llm=llm, memory=st.session_state.memory)

st.title("Asistente Personal AI - Versión 1.0")

# Input usuario
user_input = st.text_input("Escribe tu mensaje:")
if st.button("Enviar"):
    if user_input:
        response = chain.run(user_input)
        st.write("Asistente:", response)