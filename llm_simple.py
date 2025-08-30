from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

prompt = "Dame 3 consejos para aprender IA."
response = llm.invoke(prompt)
print(response.content)