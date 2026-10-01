def solution(n):
    answer = []
    t = 2
    while n != 1:
        while n % t == 0:
            n = n/t
            if t not in answer:
                answer.append(t)
        t+=1
    return answer