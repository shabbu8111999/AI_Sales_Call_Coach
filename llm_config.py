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

# Testing Block
#if __name__ == "__main__":
#    try:
        #print("Testing LLM connection...")
        #llm = get_llm_client()
        #response = llm.invoke("Say hello in one short sentence.")

        #print("Model is working!")
        #print("Response:")
        #print(response.content)

    #except Exception as e:
     #   print("Error occurred:")
      #  print(str(e))