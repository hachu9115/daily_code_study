def solution(arr, idx):
    for i,j in enumerate(arr):
        if (i >= idx) & (j == 1):
            return i
    return -1