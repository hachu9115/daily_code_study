def solution(num_list):
    odd_sum = ''
    even_sum = ''
    
    for num in num_list:
        if num % 2 == 0:  # 짝수인 경우
            even_sum += str(num)
        else:             # 홀수인 경우
            odd_sum += str(num)
    odd_sum = int(odd_sum.lstrip('0'))
    even_sum = int(even_sum.lstrip('0'))
    return odd_sum + even_sum
                                              