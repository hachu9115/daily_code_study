
def swap_case(str):
    result = []
    for i in str:
        if i.islower():
            result.append(i.upper())
        elif i.isupper():
            result.append(i.lower())
        else:
            result.append(i)
    return ''.join(result)

str = input()
output_str = swap_case(str)
print(output_str)
