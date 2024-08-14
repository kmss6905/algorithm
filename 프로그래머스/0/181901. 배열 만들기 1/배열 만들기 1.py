def solution(n, k):
    answer = []
    a = n // k
    for i in range(1, a+1):
        answer.append(i * k)
    return answer