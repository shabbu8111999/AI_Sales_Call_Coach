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
    file = request.files["audio"]

    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        report = generate_final_report()

        return jsonify({
            "transcript": open("backend/clean_transcript.txt", "r", encoding="utf-8").read(),
            "report": report
        })
    
    return jsonify({"error" : "No file uploaded"}), 400


if __name__ == "__main__":
    app.run(debug = True)