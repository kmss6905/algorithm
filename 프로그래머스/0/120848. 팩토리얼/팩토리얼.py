def factorial(n):
    if n == 1 or n== 0:
        return 1

    return n * factorial(n-1)

def solution(n):
    for i in range(1, 11):
        a = factorial(i)
        if n == a:
            return i
        if n < a:
            return i - 1