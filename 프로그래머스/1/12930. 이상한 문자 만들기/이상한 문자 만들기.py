def solution(s):
    answer = ''
    index = 0
    for j in s:
        if j == ' ':
            index = 0
            answer += j
        else:
            if index % 2 == 0:
                answer += j.upper()
            elif index % 2 == 1:
                answer += j.lower()
            index += 1
    return answer