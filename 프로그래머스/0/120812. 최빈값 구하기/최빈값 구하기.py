def solution(array):
    answer = {}
    for i in set(array):
        answer[i] = array.count(i)
    max_c = max(answer.values())
    modes = [k for k, v in answer.items() if v ==  max_c]
    return modes[0] if len(modes) ==1 else -1