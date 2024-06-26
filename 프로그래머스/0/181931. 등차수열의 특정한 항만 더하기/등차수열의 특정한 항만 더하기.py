def solution(a, d, included):
    total_sum = 0
    for i in range(len(included)):
        if included[i]:
            total_sum += a + i * d
    return total_sum