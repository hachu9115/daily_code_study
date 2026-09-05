def solution(x):
    sum_ha = 0
    for i in str(x):
        sum_ha += int(i)
    if x % sum_ha == 0:
        return True
    return False