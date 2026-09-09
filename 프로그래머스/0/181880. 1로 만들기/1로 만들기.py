def solution(num_list):
    answer = 0
    for i in num_list:
        for j in range(1,6):
            if i < 2**j:
                answer += j-1
                break
    return answer