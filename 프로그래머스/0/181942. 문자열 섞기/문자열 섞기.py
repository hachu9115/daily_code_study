def solution(str1, str2):
    answer = list(str1)
    for i, char in enumerate(str2):
        answer.insert(i*2+1,char)
    return ''.join(answer)

    
    