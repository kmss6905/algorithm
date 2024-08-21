def solution(picture, k):
    answer = []
    for i in picture:
        tmp = ''
        for idx, e in enumerate(list(i)):
            tmp += e*k

        for j in range(k):
            answer.append(tmp)
    return answer