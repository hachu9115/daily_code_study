def solution(s):
    answer = []
    memory = []
    for j,i in enumerate(s):
        if i not in memory:
            answer.append(-1)
            memory.append(i)
        elif i in memory:
            answer.append(j-(len(memory)-1-memory[::-1].index(i)))
            memory.append(i)
    return answer