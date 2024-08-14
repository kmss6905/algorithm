def solution(n):
    ls = list(str(n))
    ls.reverse()
    return list(map(int, ls))