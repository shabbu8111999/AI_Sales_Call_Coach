from flask import Flask, render_template, request, jsonify
import os
import time
import json
import uuid
import boto3
import requests
from werkzeug.utils import secure_filename
from final_report import generate_final_report

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# AWS Config
S3_BUCKET = "sales-call-audio-bucket-shabareesh"
REGION = "us-east-1"

s3 = boto3.client("s3", region_name=REGION)
transcribe = boto3.client("transcribe", region_name=REGION)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_audio():
    try:
        file = request.files.get("audio")

        if not file:
            return jsonify({"error": "No audio file provided"}), 400

        # Save locally
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        # Upload to S3
        s3.upload_file(filepath, S3_BUCKET, filename)

        media_uri = f"s3://{S3_BUCKET}/{filename}"

        # Unique Transcribe job name
        job_name = f"sales-job-{uuid.uuid4()}"

        # Start Transcription
        transcribe.start_transcription_job(
            TranscriptionJobName=job_name,
            Media={"MediaFileUri": media_uri},
            MediaFormat="mp3",
            LanguageCode="en-US",
        )

        # Wait for completion
        while True:
            status = transcribe.get_transcription_job(
                TranscriptionJobName=job_name
            )["TranscriptionJob"]["TranscriptionJobStatus"]

            if status in ["COMPLETED", "FAILED"]:
                break

            time.sleep(5)

        if status == "FAILED":
            return jsonify({"error": "Transcription failed"}), 500

        # Get transcript file URL
        transcript_url = transcribe.get_transcription_job(
            TranscriptionJobName=job_name
        )["TranscriptionJob"]["Transcript"]["TranscriptFileUri"]

        # Download transcript JSON
        response = requests.get(transcript_url)
        transcript_json = response.json()

        transcript_text = transcript_json["results"]["transcripts"][0]["transcript"]

        # Save transcript for agents
        transcript_path = "backend/clean_transcript.txt"
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(transcript_text)

        # Generate AI report
        report = generate_final_report()

        return jsonify({
            "transcript": transcript_text,
            "report": report
        })

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
