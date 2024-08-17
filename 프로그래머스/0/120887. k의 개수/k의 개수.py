def solution(i, j, k):
    answer = 0
    for m in range(i, j+1):
        for n in list(str(m)):
            if n == str(k):
                answer += 1
    return answer