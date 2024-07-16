def solution(intStrs, k, s, l):
    result = []
    for num_str in intStrs:
        substring = num_str[s:s+l]  # s번 인덱스에서 시작하는 길이 l짜리 부분 문자열
        num = int(substring)  # 부분 문자열을 정수로 변환
        if num > k:
            result.append(num)
    return result