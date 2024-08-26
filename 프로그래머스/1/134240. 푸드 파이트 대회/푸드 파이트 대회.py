def solution(food):
    answer = ''
    # food 반복 -> 각 음식의 수를 2로 나누었을 때 몫이 한쪽에 놓아질 음식의 수.
    for i in range(1, len(food)):
        if food[i] // 2 == 0:
            continue
        answer += str(i) * (food[i] // 2)
    return answer + '0' + answer[::-1]