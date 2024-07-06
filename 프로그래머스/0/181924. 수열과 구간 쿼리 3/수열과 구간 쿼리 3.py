def solution(arr, queries):
    for query in queries:
        i, j = query
        # 두 값을 서로 교환
        arr[i], arr[j] = arr[j], arr[i]
    return arr