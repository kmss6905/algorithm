def solution(number):
    answer = 0
    for i in list(number):
        answer += int(i)
    return answer % 9