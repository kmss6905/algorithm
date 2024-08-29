# 비트 연산 or
"""
1. len(arr1) 길이 만큼 반복 -> 각 인덱스에 있는 요소 끼리 비트 연산 or
2. 나온 결과를 replace 를 이용하여 #, 공백 으로 바꾼 후 answer 에 넣기
"""
def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        line = str(bin(arr1[i] | arr2[i]))[2:]
        if len(line) < n:
            line = ("0" * (n - len(line))) + line
        answer.append(line.replace("1", "#").replace("0", " "))
    return answer