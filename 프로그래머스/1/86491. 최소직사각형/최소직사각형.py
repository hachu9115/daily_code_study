def solution(sizes):
    answer = 0
    sort = []
    for i in sizes:
        sort.append(sorted(i))
    length = 0
    width = 0
    for j in sort:
        if j[0] >= length:
            length = j[0]
        if j[1] >= width:
            width = j[1]
    return length * width