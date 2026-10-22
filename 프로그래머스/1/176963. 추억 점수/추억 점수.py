def solution(name, yearning, photo):
    answer = []
    for i in photo:
        s = []
        for n,j in enumerate(name):
            if j in i:
                s.append(yearning[n])
        answer.append(sum(s))
    return answer