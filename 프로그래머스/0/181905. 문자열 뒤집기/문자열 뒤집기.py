def solution(my_string, s, e):
    # 부분 문자열을 추출하고 뒤집음
    reversed_substring = my_string[s:e+1][::-1]
    # 최종 문자열을 구성함
    result_string = my_string[:s] + reversed_substring + my_string[e+1:]
    return result_string