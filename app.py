import streamlit as st
from langchain_community.llms import LlamaCpp
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent, Tool
from langchain_community.tools import DuckDuckGoSearchRun
import logging

# Configura los logs simples
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ejemplo: Agrega logs en tu código
logging.info("Iniciando el chatbot...")  # Esto se escribe cuando corre

# En lugares donde pueda haber errores, como cargar el modelo o inicializar el agente
try:
    # *** TEMPORAL: Forza un error para probar. BORRA ESTA LÍNEA DESPUÉS DE PROBAR ***
    raise Exception("Error de prueba para chequear logs y n8n")

    # Load the model with LangChain wrapper
    llm = LlamaCpp(
        model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
        n_ctx=2048,
        n_threads=1,
        temperature=0.7,
        max_tokens=500,
        verbose=True  # For debug in terminal
    )
    logging.info("Modelo LLM cargado correctamente")
except Exception as e:
    logging.error("Ocurrió un error al cargar el LLM: " + str(e))
    st.error("Hubo un error al cargar el modelo. Revisa app.log.")

try:
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
    logging.info("Agente inicializado correctamente")
except Exception as e:
    logging.error("Ocurrió un error al inicializar el agente: " + str(e))
    st.error("Hubo un error al inicializar el agente. Revisa app.log.")

st.title("AI Assistant with Agents")

# Show conversation history
for message in st.session_state.memory.chat_memory.messages:
    st.write(f"{message.type.capitalize()}: {message.content}")

# User input
user_input = st.text_input("Enter your message:")
if st.button("Send"):
    if user_input:
        try:
            response = agent.run(user_input)
            st.write("Assistant:", response)
            logging.info("Respuesta generada correctamente para: " + user_input)
        except Exception as e:
            logging.error("Ocurrió un error al generar la respuesta: " + str(e))
            st.error("Hubo un error al procesar tu mensaje. Revisa app.log.")