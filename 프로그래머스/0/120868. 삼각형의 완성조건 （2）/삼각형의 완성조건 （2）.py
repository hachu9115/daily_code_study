def solution(sides):
    answer = 0
    result = []
    for i in range(max(sides)):
        if (max(sides) < min(sides) + i+1) and (i+1 not in result):
            result.append(i+1)
    for j in range(sum(sides)):
        if j+1 < sum(sides) and (j+1 not in result) and (j+1 > max(sides)):
            result.append(j+1)
    return len(result)