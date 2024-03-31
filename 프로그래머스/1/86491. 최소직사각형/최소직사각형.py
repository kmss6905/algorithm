def solution(sizes):
    answer = 0
    w = [] # 최대값만
    h = [] # 작은 것만
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            w.append(sizes[i][0])
            h.append(sizes[i][1])
        else:
            w.append(sizes[i][1])
            h.append(sizes[i][0])
    return max(w) * max(h)