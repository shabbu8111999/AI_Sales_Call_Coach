import time
import boto3

# Initialize Transcribe client
transcribe = boto3.client("transcribe")

# CHANGE THESE VALUES
JOB_NAME = "sales-call-transcription-job"
BUCKET_NAME = "sales-call-audio-bucket-shabareesh"
AUDIO_FILE_KEY = "Conversation.mp3"
LANGUAGE_CODE = "en-US"

# S3 file URI
MEDIA_URI = f"s3://{BUCKET_NAME}/{AUDIO_FILE_KEY}"

# Start transcription job
transcribe.start_transcription_job(
    TranscriptionJobName=JOB_NAME,
    Media={"MediaFileUri": MEDIA_URI},
    MediaFormat="mp3",
    LanguageCode=LANGUAGE_CODE,
)

print("Transcription job started...")

# Wait for job to complete
while True:
    status = transcribe.get_transcription_job(
        TranscriptionJobName=JOB_NAME
    )["TranscriptionJob"]["TranscriptionJobStatus"]

    if status in ["COMPLETED", "FAILED"]:
        break

    print("Transcribing...")
    time.sleep(10)

# Check result
job_info = transcribe.get_transcription_job(
    TranscriptionJobName=JOB_NAME
)["TranscriptionJob"]

if job_info["TranscriptionJobStatus"] == "COMPLETED":
    transcript_url = job_info["Transcript"]["TranscriptFileUri"]
    print("Transcription completed")
    print("Transcript URL:", transcript_url)
else:
    print("Transcription failed")
