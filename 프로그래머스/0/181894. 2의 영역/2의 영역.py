#  arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
def solution(arr):
    result = []
    
    if 2 not in arr:
        return [-1]
    
    for i in range(len(arr)):
        if arr[i] == 2:
            result.append(i)

    result.sort()
    return arr[result[0]: result[-1]+1]