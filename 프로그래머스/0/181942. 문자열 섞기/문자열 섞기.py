def solution(str1, str2):
    result = ""
    for i in range(len(str1)):
        result += str1[i] + str2[i]
    return result

str1 = ('첫번째 문자열을 입력하세요: ')
str2 = ('두번째 문자열을 입력하세요: ')
result = solution(str1,str2)
print(result)