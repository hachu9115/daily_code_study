def solution(numlist, n):
    distance = {}
    for i in range(len(numlist)):
        distance[numlist[i]] = n - numlist[i]
    d = sorted(distance.items(), key=lambda x: (abs(x[1]), -x[0]))
    answer = [k for k, v in d]
    return answer