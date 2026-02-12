import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

def get_llm_client():
    return ChatOpenAI(
        model = "gpt-3.5-turbo",
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )
