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


def objection_analysis(transcript_text, rag_context):
    """
    MOCKED Objection Expert reasoning (RAG-grounded)
    """
    return f"""
DETECTED OBJECTIONS:
- The customer expressed concern about pricing.
- The customer showed hesitation about committing immediately.

MISSED OPPORTUNITIES:
- The salesperson did not clearly reframe the price in terms of value.
- No strong reassurance or urgency was created.

OBJECTION HANDLING BEST PRACTICES (FROM KNOWLEDGE BASE):
{rag_context}
"""


if __name__ == "__main__":
    transcript_text = load_transcript()
    rag_context = load_rag_snapshot()

    if USE_MOCK:
        output = objection_analysis(transcript_text, rag_context)
    else:
        output = "Bedrock-based Objection Expert output"

    print("\n===== OBJECTION EXPERT AGENT OUTPUT =====\n")
    print(output)
