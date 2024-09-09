"""
1. 아이디어
BFS
2. 시간복잡도
2^20
3. 구현
ops = [1, -1]

"""
from collections import deque

def solution(numbers, target):
    answer = 0
    q = deque()
    q.append((0, numbers[0]))
    q.append((0, -numbers[0]))
    ops = [-1, 1]
    while q:
        idx, n = q.popleft()
        if idx == len(numbers) - 1:
            if n == target:
                answer += 1
            continue

        idx += 1
        for op in ops:
            next_n = n + (numbers[idx] * op)
            q.append((idx, next_n))
    
    return answer