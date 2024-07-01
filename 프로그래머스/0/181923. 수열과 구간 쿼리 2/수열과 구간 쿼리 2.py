def solution(arr, queries):
    results = []
    
    for query in queries:
        s, e, k = query
        min_value = float('inf')
        found = False
        
        for i in range(s, e + 1):
            if arr[i] > k:
                found = True
                if arr[i] < min_value:
                    min_value = arr[i]
        
        if found:
            results.append(min_value)
        else:
            results.append(-1)
    
    return results