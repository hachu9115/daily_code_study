def solution(my_string):
    answer = ''
    ban = "aeiou"
    for i in my_string:
        if i not in ban:
            answer += i
    return answer