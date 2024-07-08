def solution(num_list):
    if len(num_list) < 2:
        return num_list
    
    result = num_list
    last = num_list[-1]
    prev = num_list[-2]
    
    if last > prev:
        result.append(last - prev)
    else:
        result.append(last * 2)
    
    return result