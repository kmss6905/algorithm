def solution(arr, k):
    answer = []
    if k % 2 == 0:
        answer = [i+k for i in arr]
    else:
        answer = [i*k for i in arr]

    return answer