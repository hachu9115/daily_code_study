def solution(code):
    mode = 0
    ret = []
    
    for idx, char in enumerate(code):
        if mode == 0:
            if char == '1':
                mode = 1
            else:
                if idx % 2 == 0:
                    ret.append(char)
        elif mode == 1:
            if char == '1':
                mode = 0
            else:
                if idx % 2 != 0:
                    ret.append(char)
    
    ret_string = ''.join(ret)
    
    return ret_string if ret_string else "EMPTY"