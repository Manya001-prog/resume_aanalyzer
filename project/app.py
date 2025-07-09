from flask import Flask, render_template, request
from resume_parser import clean_text
from job_matcher import get_match_score

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume = request.files["resume"]
        jd_text = request.form["jd"]

        file_path = f"./resumes/{resume.filename}"
        resume.save(file_path)

        resume_text = open(file_path, "rb").read().decode(errors="ignore")
        clean_resume = clean_text(resume_text)
        clean_jd = clean_text(jd_text)

        score = get_match_score(clean_resume, clean_jd)
        return render_template("index.html", score=score)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
