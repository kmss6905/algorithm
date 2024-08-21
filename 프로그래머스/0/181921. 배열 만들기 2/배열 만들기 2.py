def solution(l, r):
    answer = []
    for i in range(l, r+1):
        if set(list(str(i))) == set(["0", "5"]) or set(list(str(i))) == set(["5"] or set(list(str(i))) == set(["5"])):
            answer.append(i)
    return answer if answer else [-1]