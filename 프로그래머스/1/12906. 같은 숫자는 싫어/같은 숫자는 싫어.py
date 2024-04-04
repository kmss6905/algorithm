from collections import deque

def solution(arr):
    answer = []
    q = deque(arr)
    while q:
        if len(answer) == 0:
            answer.append(q.popleft())
        else:
            e = q.popleft()
            if answer[-1] != e:
                answer.append(e)
    return answer