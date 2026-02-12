
from langchain_core.prompts import PromptTemplate
from llm_config import get_llm


def load_transcript():
    with open("backend/clean_transcript.txt", "r", encoding="utf-8") as f:
        return f.read()


def analyze_transcript(transcript_text):
    """
    Agent 1: Understand the Conversation
    """

    llm = get_llm()

    prompt_template = PromptTemplate.from_template("""
You are an expert Sales Call Transcript Analyzer.

Analyze the following transcript and answer clearly in bullet points:

1. What is the call about?
2. What is the customer's main intent?
3. What is the customer's main concern (if any)?
4. Overall tone of the conversation (positive / neutral / negative)

Be concise and structured.

Transcript:
{transcript}
""")

    # Modern LCEL chain
    chain = prompt_template | llm

    try:
        result = chain.invoke({"transcript": transcript_text})
        return result.content

    except Exception as e:
        return f"OpenAI Error: {str(e)}"


if __name__ == "__main__":
    transcript = load_transcript()
    analysis = analyze_transcript(transcript)

    print("\n TRANSCRIPT ANALYSIS ")
    print(analysis)
