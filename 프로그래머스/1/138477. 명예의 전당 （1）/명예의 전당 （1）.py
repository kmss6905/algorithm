"""
1. 명예의 전당을 관리하는 hq 
2. score 반복하면서 명예의 전당에 계속 push, 명예의 전당의 수가 K보다 작은 경우에는 마지막 원소, 큰 경우에는 k번째 점수 추가
"""
import heapq
def solution(k, score):
    answer = []
    temp = []
    for i in range(len(score)):
        temp.append(score[i])
        temp = sorted(temp, reverse=True)
        if len(temp) < k:
            answer.append(temp[-1])
        else:
            answer.append(temp[k-1])
    print(answer)
    return answer