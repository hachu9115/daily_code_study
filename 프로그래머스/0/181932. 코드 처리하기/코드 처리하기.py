def solution(code):
    mode = 0
    ret = []
    for idx, char in enumerate(code):
        if char == "1":
            mode = 1 - mode
        elif idx%2 == mode:
            ret.append(char)
    return ''.join(ret) or "EMPTY"
            
        