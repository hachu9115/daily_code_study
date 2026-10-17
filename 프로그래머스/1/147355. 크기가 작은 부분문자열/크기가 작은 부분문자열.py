def solution(t, p):
    answer = 0
    for i in range(len(t)-len(p)+1):
        string = t[i:i+len(p)]
        if int(string) <= int(p):
            answer += 1
    return answer