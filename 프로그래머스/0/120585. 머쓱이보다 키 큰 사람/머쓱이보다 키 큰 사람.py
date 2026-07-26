def solution(array, height):
    for i,j in enumerate(sorted(array)):
        if j > height:
            return len(array) - i
    return 0
        