from llama_cpp import Llama

# Load the model
llm = Llama(model_path="models/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf", n_ctx=2048, n_threads=1)

prompt = "Give me 3 tips to learn AI as a junior."
response = llm(prompt, max_tokens=500, temperature=0.7)
print("Response:", response["choices"][0]["text"])