# n 과 limit -> 약수의 개수가 limit 넘으면 중단하고 limit return, 아니면 n
# limit 만 넘으면 바로 약수 구하기 중단. 그래도 안된다. limit 가 100 이면?
# 약수의 개수를 구하는 더 간단한 방법을 찾.아.야 한다?
import math

def cnt_division(n):
    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return len(divisors)

def solution(number, limit, power):
    answer = 0
    for i in range(1, number+1):
        cnt = cnt_division(i)
        if cnt > limit:
            answer += power
            continue
        answer += cnt
    return answer

