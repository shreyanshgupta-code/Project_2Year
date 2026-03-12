import ollama

def generate_reasoning(question, k=3):
    paths = []

    for i in range(k):
        prompt = f"""
        Solve the following question step-by-step.

        Question: {question}

        Show detailed reasoning and give the final answer.
        """

        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        paths.append(response["message"]["content"])

    return paths