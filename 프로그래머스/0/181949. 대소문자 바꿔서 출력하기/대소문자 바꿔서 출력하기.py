str_input = str(input())

def switch_bs(text):
    answer = []
    for i in text:
        if i == i.upper():
            answer.append(i.lower())
        elif i != i.upper():
            answer.append(i.upper())
        else:
            print("영어가 아닌 문자가 삽입되었습니다")
    return ''.join(answer)

print(switch_bs(str_input))