def solution(a, b, c):
    answer = 0
    result = len(set([a, b, c]))
    if result == 3:
        return a+b+c
    elif result == 2:
        return (a+b+c) * (a*a + b*b + c*c)
    elif result == 1:
        return (a+b+c) * (a*a + b*b + c*c) * (a*a*a + b*b*b + c*c*c)
    return answer