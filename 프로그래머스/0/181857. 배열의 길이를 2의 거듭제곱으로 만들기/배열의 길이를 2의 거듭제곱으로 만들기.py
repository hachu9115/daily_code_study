def solution(arr):
    for i in range(11):
        if 2**i < len(arr) <= 2**(i+1):
            for j in range(2**(i+1)-len(arr)):
                arr.append(0)
    return arr