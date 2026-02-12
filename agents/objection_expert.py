# agents/objection_expert.py

from langchain_core.prompts import PromptTemplate
from llm_config import get_llm


def load_transcript():
    """Load transcript text"""
    with open("backend/clean_transcript.txt", "r", encoding="utf-8") as f:
        return f.read()


def load_rag_snapshot():
    """Lightweight RAG knowledge for production"""
    with open("backend/rag_snapshot.txt", "r", encoding="utf-8") as f:
        return f.read()


def objection_analysis(transcript_text, rag_context):
    """
    Agent 3: Objection Detection & Missed Opportunity Analysis
    Uses OpenAI via LangChain
    """

    llm = get_llm()

    prompt_template = PromptTemplate.from_template("""
You are an expert Sales Objection Handling Specialist.

Using the knowledge base below, analyze the transcript.

KNOWLEDGE BASE:
{rag_context}

TRANSCRIPT:
{transcript}

Provide structured bullet points:

1. Detected customer objections
2. Missed opportunities by the sales rep
3. How the objections should have been handled

Be clear and professional.
""")

    # Modern LCEL chain
    chain = prompt_template | llm

    try:
        result = chain.invoke({
            "transcript": transcript_text,
            "rag_context": rag_context
        })
        return result.content

    except Exception as e:
        return f"OpenAI Error: {str(e)}"


if __name__ == "__main__":
    transcript_text = load_transcript()
    rag_context = load_rag_snapshot()

    output = objection_analysis(transcript_text, rag_context)

    print("\n OBJECTION EXPERT AGENT OUTPUT \n")
    print(output)
