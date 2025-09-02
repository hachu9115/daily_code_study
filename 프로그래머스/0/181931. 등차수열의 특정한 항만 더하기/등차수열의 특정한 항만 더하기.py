def solution(a,d,included):
    answer = []
    for i, included[i] in enumerate(included):
        if included[i]:
            answer.append(a+d*i)
    return sum(answer)
    