# O(N)
# 약수 또는 인수는 어떤 수를 나누어떨어지게 하는 수를 말한다.
def solution(n):
    answer = 0
    for i in range(1, n+1):
        if n % i == 0:
            answer += i
    return answer

# 간단
def solution(n):
    answer = 0
    return sum([i for i in range(1, n+1) if n % i == 0])