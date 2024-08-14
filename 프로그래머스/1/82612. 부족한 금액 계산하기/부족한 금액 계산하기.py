def solution(price, money, count):
    answer = -1
    total_price = 0
    for i in range(1, count+1):
        total_price += price * i
    print(total_price)
    return total_price - money if total_price > money else 0