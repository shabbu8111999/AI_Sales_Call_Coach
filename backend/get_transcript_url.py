import boto3

# CHANGE THIS to the job name you used earlier
JOB_NAME = "sales-call-transcription-job"

transcribe = boto3.client("transcribe")

response = transcribe.get_transcription_job(
    TranscriptionJobName=JOB_NAME
)

job = response["TranscriptionJob"]

if job["TranscriptionJobStatus"] == "COMPLETED":
    transcript_url = job["Transcript"]["TranscriptFileUri"]
    print("Transcript URL found:")
    print(transcript_url)
else:
    print("Job not completed or not found")
