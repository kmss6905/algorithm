def isCube(l):
    while l % 2 == 0:
        l //= 2

    if l == 1:
        return True
    else:
        return False

# 2의 거듭제곱인 것을 판단
def solution(arr):
    zc = []
    answer = []
    l = len(arr)
    while True:
        if isCube(l):
            break
        arr += [0]
        l += 1
    
    return arr
    