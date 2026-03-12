from flask import Flask, render_template, request
from generator import generate_reasoning
from selector import select_best

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    results = None
    best = None

    if request.method == "POST":

        question = request.form["question"]

        paths = generate_reasoning(question)

        results, best = select_best(paths)

    return render_template("index.html", results=results, best=best)

if __name__ == "__main__":
    app.run(debug=True)
    