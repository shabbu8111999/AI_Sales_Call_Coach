from flask import Flask, render_template, request, jsonify
import os
from final_report import generate_final_report


app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_audio():
    try:
        file = request.files.get("audio")

        if not file:
            return jsonify({"error": "No audio file provided"}), 400

        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # We are NOT re-running Transcribe in production demo
        # We reuse pre-generated transcript safely
        transcript_path = "backend/clean_transcript.txt"

        if not os.path.exists(transcript_path):
            return jsonify({"error": "Transcript file not found on server"}), 500

        transcript = open(transcript_path, "r", encoding="utf-8").read()
        report = generate_final_report()

        return jsonify({
            "transcript": transcript,
            "report": report
        })

    except Exception as e:
        print("UPLOAD ERROR:", str(e))
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    #app.run(debug = True)
    app.run(host="0.0.0.0", port=5000)