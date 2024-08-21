def solution(intStrs, k, s, l):
    answer = []
    for e in intStrs:
        cut_number = int(e[s:s+l])
        if cut_number > k:
            answer.append(cut_number)
    return answer