def solution(a, b):
    answer = 0
    ab = a * b
    if ab % 2 != 0:
        return a*a + b*b
    else:
        if a % 2 == 0 and b % 2 == 0:
            return abs(a - b)
        else:
            # 하나라도 홀수
            return 2 * (a + b)