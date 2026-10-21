from math import gcd

def solution(a, b):
    d = b // gcd(a, b) 

    for p in (2, 5):
        while d % p == 0:
            d //= p

    return 1 if d == 1 else 2