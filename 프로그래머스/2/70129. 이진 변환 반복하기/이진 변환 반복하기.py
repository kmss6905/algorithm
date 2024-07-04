def solution(s):
    zc = 0
    cc = 0
    while s != '1':
        after = s.replace('0', '')
        zc += len(s) - len(after)
        s = bin(len(after)).replace('0b', '')
        cc += 1
    return [cc, zc]