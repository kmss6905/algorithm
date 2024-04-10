def solution(s):
    a = 0
    c = 0
    while s != '1':
        zerocnt = 0
        for i in s:
            if i == '0':
                zerocnt += 1
        c += zerocnt
        a += 1
        s = str(bin(len(s) - zerocnt))[2::]
    return [a, c]