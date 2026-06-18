from flask import Flask, render_template, request
from recorder import transcribe_audio
from formatter import format_update
from jira_client import post_comment

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/process", methods=["POST"])
def process():
    issue_key = request.form["issue_key"]
    audio = request.files["audio"]

    temp_file = "temp.wav"
    audio.save(temp_file)

    text = transcribe_audio(temp_file)
    comment = format_update(text)

    if request.form.get("post_to_jira"):
        post_comment(issue_key, comment)

    return render_template(
        "index.html",
        transcript=text,
        comment=comment,
        issue_key=issue_key
    )

if __name__ == "__main__":
    app.run(debug=True)
