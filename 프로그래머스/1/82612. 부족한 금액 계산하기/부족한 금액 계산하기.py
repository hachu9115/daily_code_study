def solution(price, money, count):
    while count != 0:
        money = money - price*count
        count -= 1
    return abs(money) if money < 0 else 0