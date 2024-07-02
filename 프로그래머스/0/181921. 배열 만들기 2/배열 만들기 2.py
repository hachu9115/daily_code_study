def solution(l, r):
    result = []

    for number in range(l, r + 1):
        str_number = str(number)
        if all(ch in '05' for ch in str_number):
            result.append(number)

    if not result:
        return [-1]
    else:
        return sorted(result)