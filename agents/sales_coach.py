from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


USE_MOCK = True


def load_transcript():
    """Load pre-generated transcript"""
    with open("backend/clean_transcript.txt", "r", encoding="utf-8") as f:
        return f.read()


def load_rag_snapshot():
    """Lightweight RAG knowledge for production demo"""
    with open("backend/rag_snapshot.txt", "r", encoding="utf-8") as f:
        return f.read()


def sales_coach_analysis(transcript_text, rag_context):
    """
    MOCKED Sales Coach reasoning (RAG-grounded)
    """
    return f"""
WHAT WENT WELL:
- The salesperson introduced the product clearly.
- The tone was polite and professional.

WHAT NEEDS IMPROVEMENT:
- More discovery questions could have been asked to better understand the customer's needs.
- A stronger closing attempt was missing.

SALES BEST PRACTICES (FROM KNOWLEDGE BASE):
{rag_context}
"""


if __name__ == "__main__":
    transcript_text = load_transcript()
    rag_context = load_rag_snapshot()

    if USE_MOCK:
        output = sales_coach_analysis(transcript_text, rag_context)
    else:
        output = "Bedrock-based Sales Coach output"

    print("\n===== SALES COACH AGENT OUTPUT =====\n")
    print(output)
