import math
def solution(n, m):
    answer = []
    g = math.gcd(n,m)
    answer.append(g)
    answer.append(n*m//g)

    return answer