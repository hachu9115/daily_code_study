def solution(a, b):
    answer1 = str(a) + str(b)
    answer2 = 2 * a * b
    return max(int(answer1), answer2)