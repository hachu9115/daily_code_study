def solution(a,b):
    c = str(a)
    d = str(b)
    if (c+d)<(d+c):
        return int(d+c)
    else:
        return int(c+d)
    

    