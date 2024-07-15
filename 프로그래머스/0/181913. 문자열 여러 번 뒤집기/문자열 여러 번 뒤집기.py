def solution(my_string, queries):
    # my_string을 리스트로 변환 (문자열은 불변형이므로 리스트로 변환 후 조작)
    my_list = list(my_string)
    
    # queries에 따라 부분 문자열 뒤집기 수행
    for s, e in queries:
        # 부분 리스트를 뒤집어서 다시 할당
        my_list[s:e+1] = my_list[s:e+1][::-1]
    
    # 리스트를 다시 문자열로 변환하여 반환
    return ''.join(my_list)