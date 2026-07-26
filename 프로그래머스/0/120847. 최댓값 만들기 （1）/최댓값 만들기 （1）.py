def solution(numbers):
    n = len(numbers)
    
    return sorted(numbers)[n-1] * sorted(numbers)[n-2]