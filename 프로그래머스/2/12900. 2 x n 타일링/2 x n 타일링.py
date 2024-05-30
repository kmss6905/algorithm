def solution(n):
    b = [0] * 60000
    b[1] = 1
    b[2] = 2
    b[3] = 3
    
    for i in range(4, n+1):
        b[i] = (b[i-1] + b[i-2]) % 1000000007

    return b[n] % 1000000007