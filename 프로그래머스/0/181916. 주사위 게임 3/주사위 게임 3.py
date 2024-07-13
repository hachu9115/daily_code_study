def solution(a, b, c, d):
    from collections import Counter
    counts = Counter([a, b, c, d])
    if len(counts) == 1:
        # 모든 숫자가 같은 경우
        p = a
        return 1111 * p
    elif len(counts) == 2:
        # 세 숫자가 같은 경우와 두 숫자가 같은 경우를 구분
        p, q = counts.keys()
        if counts[p] == 3:
            return (10 * p + q) ** 2
        elif counts[q] == 3:
            return (10 * q + p) ** 2
        else:
            # 두 숫자가 두 개씩 나오는 경우
            return (p + q) * abs(p - q)
    elif len(counts) == 3:
        # 두 숫자가 같은 경우 (한 숫자가 두 개, 다른 두 숫자가 각각 하나)
        p = [num for num in counts if counts[num] == 2][0]
        q, r = [num for num in counts if counts[num] == 1]
        return q * r
    else:
        # 모든 숫자가 다른 경우
        return min(a, b, c, d)