def solution(angle):
    answer = 0
    if angle / 90 < 1:
        answer = 1
    elif 2> angle / 90 > 1:
        answer = 3
    else:
        answer = 2*(angle / 90)
    return answer