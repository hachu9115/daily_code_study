def solution(arr):
    answer = []
    if 2 in arr:
        i = arr.index(2)
        j = arr[::-1].index(2)
        return arr[i:len(arr)-j]
    else:
        return [-1]