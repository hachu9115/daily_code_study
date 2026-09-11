def solution(emergency):
    ranks = {v: i + 1 for i, v in enumerate(sorted(emergency, reverse=True))}
    return [ranks[v] for v in emergency]