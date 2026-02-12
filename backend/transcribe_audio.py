import time
import boto3
import uuid
import requests
import json

# Initialize Transcribe client
transcribe = boto3.client("transcribe", region_name="us-east-1")

# CONFIG
BUCKET_NAME = "sales-call-audio-bucket-shabareesh"
AUDIO_FILE_KEY = "Conversation.mp3"

# Generate unique job name
JOB_NAME = f"sales-call-job-{uuid.uuid4()}"

# Get file extension dynamically
file_extension = AUDIO_FILE_KEY.split(".")[-1].lower()

MEDIA_URI = f"s3://{BUCKET_NAME}/{AUDIO_FILE_KEY}"

# Start transcription job
transcribe.start_transcription_job(
    TranscriptionJobName=JOB_NAME,
    Media={"MediaFileUri": MEDIA_URI},
    MediaFormat=file_extension,
    IdentifyLanguage=True
)

print("Transcription job started...")

# Wait for completion
while True:
    status = transcribe.get_transcription_job(
        TranscriptionJobName=JOB_NAME
    )["TranscriptionJob"]["TranscriptionJobStatus"]

    if status in ["COMPLETED", "FAILED"]:
        break

    print("Transcribing...")
    time.sleep(5)

if status == "FAILED":
    print("Transcription failed")
else:
    transcript_url = transcribe.get_transcription_job(
        TranscriptionJobName=JOB_NAME
    )["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]

    print("Transcription completed")
    print("Transcript URL:", transcript_url)

    # Download transcript
    response = requests.get(transcript_url)
    transcript_json = response.json()

    transcript_text = transcript_json["results"]["transcripts"][0]["transcript"]

    # Save locally
    with open("backend/clean_transcript.txt", "w", encoding="utf-8") as f:
        f.write(transcript_text)

    print("Transcript saved to backend/clean_transcript.txt")
