import re

def solution(myStr):
    answer = [x for x in re.split(r"[abc]", myStr) if x]
    return answer if answer else ["EMPTY"]