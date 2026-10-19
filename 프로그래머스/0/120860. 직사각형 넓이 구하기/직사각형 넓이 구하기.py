def solution(dots):
    answer = 0
    print(max(dots)[0])
    print(min(dots)[0])
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])