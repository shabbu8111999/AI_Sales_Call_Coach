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
    return FAISS.load_local("vector_db", embeddings, allow_dangerous_deserialization=True)


def query_sales_knowledge(vector_db, query):
    docs = vector_db.similarity_search(query, k=3)
    return "\n".join([doc.page_content for doc in docs])


def sales_coach_analysis(transcript_text, rag_context):
    """
    MOCKED Sales Coach reasoning
    """
    return f"""
WHAT WENT WELL:
- The salesperson introduced the product clearly.
- The tone was polite and professional.

WHAT NEEDS IMPROVEMENT:
- More discovery questions could have been asked to understand the customer's needs better.
- A strong closing attempt was missing.

SALES BEST PRACTICES(FROM KNOWLEDGE BASE):
{rag_context}
    """


if __name__ == "__main__":
    transcript = load_transcript()
    vector_db = load_rag()

    rag_context = query_sales_knowledge(
        vector_db,
        "sales discovery questions and closing techniques"
    )

    if USE_MOCK:
        output = sales_coach_analysis(transcript, rag_context)
    else:
        output = "Bedrock-based Sales Coach output"

    print("Sales Coach Agent Output:")
    print(output)