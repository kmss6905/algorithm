def countOne(n):
    cnt = 0
    for i in bin(n).strip('0b'):
        if int(i) == 1:
            cnt += 1
    return cnt

def solution(n):
    answer = 0
    ncount = countOne(n)
    a = n + 1
    while True:
        if countOne(n) == countOne(a):
            answer = a
            break
        a += 1
    return answer

