def solution(arr, idx):
    answer = 0
    for i in range(len(arr)):
        if idx <= i and arr[i] == 1:
            return i
    return -1