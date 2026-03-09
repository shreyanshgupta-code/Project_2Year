from reasoning_generator import generate_reasoning
from self_critic import score_reasonings
from selector import select_best


def solve(question):

    print("Generating reasoning paths...\n")

    reasonings = generate_reasoning(question)

    for i, r in enumerate(reasonings):
        print(f"\nReasoning {i+1}:\n{r}\n")

    scores = score_reasonings(reasonings)

    print("Scores:", scores)

    best = select_best(reasonings, scores)

    print("\nBest Reasoning:\n")
    print(best)


if __name__ == "__main__":

    question = input("Enter question: ")

    solve(question)