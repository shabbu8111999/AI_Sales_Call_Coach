import boto3
import json
import os

# Using real Bedrock (no mock)
USE_MOCK = False

# Initialize Bedrock runtime client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
)

MODEL_ID = "mistral.mistral-large-2402-v1:0"


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
    Powered by AWS Bedrock (Mistral)
    """

    prompt = f"""
You are an expert Sales Objection Handling Specialist.

Using the knowledge base below, analyze the transcript.

KNOWLEDGE BASE:
{rag_context}

TRANSCRIPT:
{transcript_text}

Provide structured bullet points:

1. Detected customer objections
2. Missed opportunities by the sales rep
3. How the objections should have been handled
Be clear and professional.
"""

    body = {
        "prompt": prompt,
        "max_tokens": 700,
        "temperature": 0.3
    }

    try:
        response = bedrock.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(body),
            contentType="application/json",
            accept="application/json"
        )

        response_body = json.loads(response["body"].read())

        # Mistral response format
        return response_body["outputs"][0]["text"]

    except Exception as e:
        return f"Bedrock Error: {str(e)}"


if __name__ == "__main__":
    transcript_text = load_transcript()
    rag_context = load_rag_snapshot()

    output = objection_analysis(transcript_text, rag_context)

    print("\n===== OBJECTION EXPERT AGENT OUTPUT =====\n")
    print(output)
