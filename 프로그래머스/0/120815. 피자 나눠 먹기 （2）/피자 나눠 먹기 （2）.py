def solution(n):
    a = 1
    while 6*a % n != 0:
        a += 1
    return a