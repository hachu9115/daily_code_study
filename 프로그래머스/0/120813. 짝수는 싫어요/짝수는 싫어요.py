def solution(n):
    answer = []
    for i in range(n):
        if (i+1) % 2 ==1:
            answer.append(i+1)
    return sorted(answer)