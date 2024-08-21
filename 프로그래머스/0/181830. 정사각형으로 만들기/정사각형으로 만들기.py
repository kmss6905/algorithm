def solution(arr):
    n, m = len(arr), len(arr[0])
    if n > m:
        for i in range(n):
            arr[i] += ([0] * (abs(m-n)))
    elif n < m:
        arr += ([[0] * m] * (abs(m-n)))
    return arr