def solution(a, b):
    carry = 0
    result = []
    i, j  = len(a)-1, len(b)-1
    while i >=0 or j >=0 or carry:
        s = carry
        if i>=0:
            s += int(a[i])
            i -= 1
        if j>=0:
            s += int(b[j])
            j -= 1
        result.append(str(s%10))
        carry = s //10
    
    return ''.join(reversed(result))