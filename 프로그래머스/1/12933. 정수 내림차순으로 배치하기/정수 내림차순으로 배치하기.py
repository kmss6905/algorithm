def solution(n):
    ls = sorted(list(str(n)), reverse=True)
    return int(''.join(ls))