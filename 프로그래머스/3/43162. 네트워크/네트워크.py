from collections import deque
'''
비슷한 유형 -> 섬의 개수를 구하라: 전형적인 BFS/DFS 문제
다만, 다른 점은, 주어진 조건을 조금 변형해야한다.

섬의 개수는 주어진 행렬(이중 리스트) 그대로 사용하는 반면에
이 문제는 문제 해석 -> 활용할 수 있도록 그래프를 직접 구현해야함.

조금 어렵다고 하는 문제 특징
1. 문제 해석 -> 그래프 적인 특징 파악 -> 그래프 직접 구현(여기서 얼마나 까다롭게 하는 것에서도 차이가 있는 듯)
'''
def solution(n, computers):
    answer = 0
    graph = {}
    # 1. 그래프 구현
    for i in range(n):
        for j in range(n):
            if i not in graph:
                graph[i] = []

            if i != j and computers[i][j] == 1:
                graph[i].append(j)
        
    
    visited = {}
    def bfs(graph, start_v):
        q = deque()
        
        # 첫 네트워크 방문
        q.append(start_v)
        visited[start_v] = True
        while q:
            cur_v = q.popleft() 
            for v in graph[cur_v]:
                if v not in visited:
                    visited[v] = True # 방문한 네트워크 기록
                    q.append(v) # 다음 방문할 네트워크 큐에 append
    
    network = 0
    for i in graph:
        if i not in visited:
            bfs(graph, i) # BFS 탐색
            network += 1  # 네트워크 수 1 증가
        
    return network