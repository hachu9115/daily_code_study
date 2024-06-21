def solution(a, b):
    SA = str(a)
    SB = str(b)
    AB = SA + SB
    BA = SB + SA
    IAB = int(AB)
    IBA = int(BA)
    return max(IAB, IBA)

    