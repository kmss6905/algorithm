def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        res = 1000000
        for i in range(s, e+1):
            if arr[i] > k:
                res = min(res, arr[i])
        res = -1 if res == 1000000 else res
        answer.append(res)
        
    return answer