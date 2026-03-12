import ollama

def score_reasoning(reasoning):

    prompt = f"""
    Evaluate the following reasoning.

    Score from 1 to 10 based on:
    - logical correctness
    - clarity
    - completeness

    Only return the number.

    Reasoning:
    {reasoning}
    """

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    score = response["message"]["content"]

    try:
        score = float(score.strip())
    except:
        score = 5

    return score