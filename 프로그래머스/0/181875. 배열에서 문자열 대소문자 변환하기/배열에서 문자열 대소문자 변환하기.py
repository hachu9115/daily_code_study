def solution(strArr):
    answer = []
    for i,j in enumerate(strArr):
        if i == 0 or i % 2 == 0:
            answer.append(j.lower())
        else:
            answer.append(j.upper())
    return answer