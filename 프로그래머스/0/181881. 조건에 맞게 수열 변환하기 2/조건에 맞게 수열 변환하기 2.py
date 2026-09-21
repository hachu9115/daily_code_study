def solution(arr):
    answer = 0
    while True:
        new = []
        for v in arr:
            if v >= 50 and v % 2 == 0:
                new.append(v // 2)
            elif v < 50 and v % 2 == 1:
                new.append(v * 2 + 1)
            else:
                new.append(v)
        if new == arr:
            return answer
        arr = new
        answer += 1