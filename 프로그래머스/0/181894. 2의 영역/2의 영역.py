def solution(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == 2:
            result.append(i)
    
    if len(result) == 0:
        return [-1]
    
    result = sorted(result)
    answer = []
    for i in range(result[0], result[-1]+1):
        answer.append(arr[i])
    
    return answer