def solution(age):
    answer = ''
    for _ in str(age):
        for i,j in enumerate("abcdefghij"):
            if int(_) == i:
                answer += j
    return answer