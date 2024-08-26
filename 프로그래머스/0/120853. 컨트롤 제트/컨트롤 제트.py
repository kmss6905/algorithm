def solution(s):
    answer = 0
    l = s.split(" ")
    for idx, e in enumerate(l):
        if e == 'Z':
            answer -= int(l[idx-1])
            continue
        answer += int(e)

    return answer