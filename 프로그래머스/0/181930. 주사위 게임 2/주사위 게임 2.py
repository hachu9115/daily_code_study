def solution(a, b, c):
    # Case 1: 모든 숫자가 다를 때
    if a != b and b != c and a != c:
        return a + b + c
    
    # 각 숫자의 제곱과 세제곱 계산
    sum_of_squares = a**2 + b**2 + c**2
    sum_of_cubes = a**3 + b**3 + c**3
    
    # Case 2: 두 숫자가 같고 하나가 다를 때
    if (a == b and b != c) or (a == c and b != c) or (b == c and a != b):
        return (a + b + c) * sum_of_squares
    
    # Case 3: 세 숫자가 모두 같을 때
    if a == b == c:
        return (a + b + c) * sum_of_squares * sum_of_cubes