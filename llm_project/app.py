from time import perf_counter

from flask import Flask, render_template, request

from generator import DEFAULT_REASONING_PATHS, generate_reasoning
from selector import select_best

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    best = None
    question = ""
    answer_mode = "fast"
    error = None
    metrics = None

    if request.method == "POST":
        question = request.form["question"].strip()
        answer_mode = request.form.get("answer_mode", "fast")

        if question:
            started_at = perf_counter()

            try:
                paths = generate_reasoning(
                    question,
                    k=DEFAULT_REASONING_PATHS,
                    mode=answer_mode,
                )
                results, best = select_best(paths)
                metrics = {
                    "path_count": len(results),
                    "elapsed_seconds": round(perf_counter() - started_at, 2),
                    "answer_mode": answer_mode.title(),
                }
            except Exception as exc:
                error = f"Request failed: {exc}"
        else:
            error = "Please enter a question."

    return render_template(
        "index.html",
        results=results,
        best=best,
        question=question,
        answer_mode=answer_mode,
        error=error,
        metrics=metrics,
    )


if __name__ == "__main__":
    app.run(debug=True)
