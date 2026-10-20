from collections import Counter

def solution(number):
    answer = 0
    for i in range(len(number)):
        seen = Counter()
        for j in range(i + 1, len(number)):
            answer += seen[-(number[i] + number[j])]
            seen[number[j]] += 1    
    return answer