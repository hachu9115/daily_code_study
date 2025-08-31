def evenfunc(number):
    if number%2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"
        
print(evenfunc(int(input())))
