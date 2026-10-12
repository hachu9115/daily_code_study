def solution(balls, share):
    answer = 1
    for i in range(share):
        answer = answer * (balls - i) // (i + 1)
    return answer