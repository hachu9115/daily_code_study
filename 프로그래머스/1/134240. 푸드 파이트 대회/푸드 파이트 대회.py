def solution(food):
    answer = ''
    for i,j in enumerate(food):
        if i > 0 and j >= 2:
            answer += str((i))*(j//2)
    answer += '0'
    plus = answer[len(answer)-2::-1]
    answer = answer + plus
    return answer