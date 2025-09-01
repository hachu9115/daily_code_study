def solution(n):
    if n%2 ==1:
        return sum(i*2+1 for i in range((n//2)+1))
    else:
        return sum((i*2+2)**2 for i in range(n//2))
