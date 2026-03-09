import requests
from config import MODEL, NUM_REASONING_PATHS

OLLAMA_URL = "http://localhost:11434/api/generate"


def generate_reasoning(question):

    reasonings = []

    prompt = f"""
Solve step by step.

Question: {question}

Reasoning:
"""

    for _ in range(NUM_REASONING_PATHS):

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False,
                "temperature": 0.8
            }
        )

        result = response.json()["response"]

        reasonings.append(result)

    return reasonings