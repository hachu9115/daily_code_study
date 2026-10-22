def solution(strings, n):
    answer = []
    sort = []
    for i in strings:
        sort.append(i[n])
    for j in sorted(sort):
        for m in sorted(strings):
            if m[n] == j and m not in answer:
                answer.append(m)
    return answer