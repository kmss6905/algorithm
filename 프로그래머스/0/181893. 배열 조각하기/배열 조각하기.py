# query 순회, index range 로 순회
# cut = query[i]
# arr[:cut+1]
# arr[cut+1:]
def solution(arr, query):
    for i in range(len(query)):
        cut = query[i]
        if i % 2 == 0:
            arr = arr[:cut+1]
        else:
            arr = arr[cut:]

    return arr