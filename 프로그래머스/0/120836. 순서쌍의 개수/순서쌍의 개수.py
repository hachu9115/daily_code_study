def solution(n):
    answer = 0
    for i in range(n//2):
        if n % (i+1) == 0:
            answer+=1        
    return answer+1