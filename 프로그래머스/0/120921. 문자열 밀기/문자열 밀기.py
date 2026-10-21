def solution(A, B):
    for i in range(len(A)):
        if (A[len(A)-i:len(A)]+A[0:len(A)-i]) == B:
            return i
    return -1