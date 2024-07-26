def solution(my_string, is_prefix):
    # my_string의 처음부터 is_prefix 길이만큼 자른 부분과 is_prefix를 비교
    if my_string[:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0