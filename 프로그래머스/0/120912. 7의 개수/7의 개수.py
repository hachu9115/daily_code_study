def solution(array):
    ans = ''
    for i in array:
        ans += str(i)
    return ans.count('7')