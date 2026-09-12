import re
def solution(my_string):
    return sum(int(n) for n in re.findall(r'\d+', my_string))