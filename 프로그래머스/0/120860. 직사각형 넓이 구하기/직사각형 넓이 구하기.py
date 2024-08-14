def solution(dots):
    answer = 0
    xs = []
    ys = []
    for i in dots:
        xs.append(i[0])
        ys.append(i[1])
    
    xs = list(set(xs))
    ys = list(set(ys))
    return abs(xs[0] - xs[1]) * abs(ys[0] - ys[1])