from flask import Flask, render_template, redirect, g, url_for, request

import model

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")
    
@app.route("/get_student")
def show_student():
    github = request.args.get("github", "chriszf")
    s = model.get_student_by_github(github)
    return render_template("show_student.html",
            student = s)


if __name__ == "__main__":
    app.run(debug=True)
