import boto3
import json
import os

# No more mock mode
USE_MOCK = False

# Initialize Bedrock runtime client
bedrock = boto3.client(
    service_name="bedrock-runtime",
    region_name=os.environ.get("AWS_DEFAULT_REGION", "us-east-1")
)

MODEL_ID = "mistral.mistral-large-2402-v1:0"


def load_transcript():
    """Read Clean Transcript text"""
    with open("backend/clean_transcript.txt", "r", encoding="utf-8") as f:
        return f.read()


def analyze_transcript(transcript_text):
    """Agent 1: Understand the Conversation using AWS Bedrock (Mistral)"""

    prompt = f"""
You are an expert Sales Call Transcript Analyzer.

Analyze the following transcript and answer clearly in bullet points:

1. What is the call about?
2. What is the customer's main intent?
3. What is the customer's main concern (if any)?
4. Overall tone of the conversation (positive / neutral / negative)

Be concise and structured.

Transcript:
{transcript_text}
"""

    body = {
        "prompt": prompt,
        "max_tokens": 600,
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

        # Mistral format
        return response_body["outputs"][0]["text"]

    except Exception as e:
        return f"Bedrock Error: {str(e)}"


if __name__ == "__main__":
    transcript = load_transcript()

    analysis = analyze_transcript(transcript)

    print("===== TRANSCRIPT ANALYSIS =====")
    print(analysis)
