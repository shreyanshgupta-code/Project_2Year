from critic import score_reasoning

def select_best(paths):

    results = []

    for p in paths:

        score = score_reasoning(p)

        results.append({
            "reasoning": p,
            "score": score
        })

    best = max(results, key=lambda x: x["score"])

    return results, best