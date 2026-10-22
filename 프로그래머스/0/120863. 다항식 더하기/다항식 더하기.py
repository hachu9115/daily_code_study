def solution(polynomial):
    x_sum, c_sum = 0, 0
    for term in polynomial.split(' + '):
        if term.endswith('x'):
            coef = term[:-1]
            x_sum += int(coef) if coef else 1
        else:
            c_sum += int(term)

    parts = []
    if x_sum:
        parts.append('x' if x_sum == 1 else f'{x_sum}x')
    if c_sum:
        parts.append(str(c_sum))
    return ' + '.join(parts) or '0'