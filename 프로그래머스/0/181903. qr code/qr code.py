def solution(q, r, code):
    answer = ''
    for idx, e in enumerate(list(code)):
        if idx % q == r:
            answer += e
    return answer