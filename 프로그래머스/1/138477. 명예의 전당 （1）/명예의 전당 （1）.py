def solution(k, score):
    answer = []
    an = []
    for i in score:
        if len(answer) < k:
            answer.append(i)
        elif i > min(answer):
            answer.remove(min(answer))
            answer.append(i)
        an.append(min(answer))
    return an