def solution(myString, pat):
    a = pat.upper() in myString.upper()
    return int(a)