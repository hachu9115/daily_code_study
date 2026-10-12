def solution(my_string):
    answer = 0
    split = my_string.split()
    for i in range(len(split)):
        if i == 0:
            answer += int(split[i])
        elif split[i] == "+":
            answer += int(split[i+1])
        elif split[i] == '-':
            answer -= int(split[i+1])
    return answer