def solution(myString, pat):
    n = len(myString)
    string = myString[::-1]
    for i in range(n):
        if string[i:i+len(pat)] == pat[::-1]:
            return myString[:n-i]