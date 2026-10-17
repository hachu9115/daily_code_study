def solution(rank, attendance):
    answer = 0
    save1 = []
    for i,j in enumerate(attendance):
        if j == True:
            save1.append(rank[i])
    save2 = sorted(save1)
    return rank.index(save2[0]) * 10000 + rank.index(save2[1]) * 100 + rank.index(save2[2])