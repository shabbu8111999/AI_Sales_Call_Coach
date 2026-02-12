
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


def sales_coach_analysis(transcript_text, rag_context):
    """
    Agent 2: Sales Coaching Analysis
    Uses OpenAI via LangChain
    """

    llm = get_llm()

    prompt_template = PromptTemplate.from_template("""
You are an expert Sales Coach.

Using the knowledge base below, evaluate the sales representative's performance.

KNOWLEDGE BASE:
{rag_context}

TRANSCRIPT:
{transcript}

Provide structured bullet points under these sections:

1. What went well
2. What needs improvement
3. Missed opportunities
4. Recommended improvements

Be professional and actionable.
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

    output = sales_coach_analysis(transcript_text, rag_context)

    print("\nSALES COACH AGENT OUTPUT\n")
    print(output)
