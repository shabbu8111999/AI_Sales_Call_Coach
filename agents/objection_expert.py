from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


USE_MOCK = True


def load_transcript():
    with open("backend/clean_transcript.txt", "r", encoding="utf-8") as f:
        return f.read()
    

def load_rag():
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    return FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )


def query_objection_knowledge(vector_db):
    docs = vector_db.similarity_search(
        "handling price objections and customer hesitation", k=3
    )
    return "\n".join([doc.page_content for doc in docs])


def objection_analysis(transcript_text, rag_context):
    """
    MOCKED Objection Expert reasoning
    """
    return f"""
DETECTED OBJECTIONS:
- The customer expressed concern about pricing.
- The customer showed hesitation about committing immediately.

MISSED OPPORTUNITIES:
- The salesperson did not clearly reframe the price in terms of value.
- No strong reassurance or urgency was created.

OBJECTION HANDLING BEST PRACTICES(FROM KNOWLEDGE BASE):
{rag_context}
    """


if __name__ == "__main__":
    transcript_text = load_transcript()
    vector_db = load_rag()

    rag_context = query_objection_knowledge(vector_db)

    if USE_MOCK:
        output = objection_analysis(transcript_text, rag_context)
    else:
        output = "Bedrock-based Objection Expert output"

    print("Objection Expert Agent Output:")
    print(output)