def solution(n):
    answer = []
    for i in range(n):
        b = [0 for _ in range(n)]
        b[i] = 1
        answer.append(b)
    return answer