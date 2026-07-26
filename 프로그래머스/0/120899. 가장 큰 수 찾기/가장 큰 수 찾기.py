def solution(array):
    answer = []
    for i,j in enumerate(array):
        if j == max(array):
            return [j,i]