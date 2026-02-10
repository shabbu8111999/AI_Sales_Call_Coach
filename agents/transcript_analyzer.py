import boto3
import json

USE_MOCK = True

# Initializing Bedrock runtime client
bedrock = boto3.client(
    service_name = "bedrock-runtime",
    region_name = "us-east-1"
)

MODEL_ID = "mistral.mistral-large-2402-v1:0"


def load_transcript():
    """Read Clean Transcript text"""
    with open("backend/clean_transcript.txt", "r", encoding="utf-8") as f:
        return f.read()
    

def analyze_transcript(transcript_text):
    """Agent 1: Understand the Conversation"""

    prompt = f"""
You are a Transcript Analyzer AI.

Read the sales call transcript below and answer clearly in simple bullet points:

1. What is the call about?
2. What is the customer's main intent?
3. What is the customer's main concern (if any)?
4. Overall tone of the conversation (positive / neutral / negative)

Transcript:
{transcript_text}
"""
    
    body = {
        "prompt" : prompt,
        "max_tokens" : 400,
        "temperature" : 0.3
    }


    response = bedrock.invoke_model(
        modelId = MODEL_ID,
        body = json.dumps(body),
        contentType = "application/json",
        accept = "application/json"
    )


    response_body = json.loads(response["body"].read())
    return response_body["outputs"][0]["text"]


if __name__ == "__main__":
    transcript = load_transcript()

    if USE_MOCK:

        analysis = """
    - The call is about a product introduction and pricing discussion.
    - The customer shows interest but is cautious.
    - The main concern is pricing and timing.
    - The overall tone is neutral with hesitation.
    """
    else:
        analysis = analyze_transcript(transcript)

    print("Transcript Analysis:")
    print(analysis)