def solution(numLog):
    # 조작을 위한 문자열을 저장할 변수
    operations = ''
    
    # numLog 배열의 연속된 두 값의 차이를 계산
    for i in range(1, len(numLog)):
        difference = numLog[i] - numLog[i-1]
        
        # 차이에 따라 해당되는 조작을 문자열에 추가
        if difference == 1:
            operations += 'w'
        elif difference == -1:
            operations += 's'
        elif difference == 10:
            operations += 'd'
        elif difference == -10:
            operations += 'a'
    
    return operations