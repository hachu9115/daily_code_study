def solution(before, after):
    for i in after:
        if after.count(i) != before.count(i):
            return 0
    return 1