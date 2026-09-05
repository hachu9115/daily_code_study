def solution(n):
    answer = []
    num = [2]
    for i in range(1,n+1):
        count = 0
        if i not in answer:
            for j in range(1,i+1):
                if i % j == 0:
                    count += 1
                if count == 3:
                    answer.append(i)
        
    return len(set(answer))
            
            
                