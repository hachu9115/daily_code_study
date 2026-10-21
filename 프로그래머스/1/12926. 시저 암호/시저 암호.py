def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer += ' '
        elif (ord(i) + n) > 122 and 97 <= ord(i) <= 122: 
            answer += chr(97+ ord(i) + n -123)
        elif (ord(i) + n) > 90 and 65 <= ord(i) <= 90:
            answer += chr(65+ ord(i) + n -91)
        else:
            answer += chr(ord(i) + n)
    return answer