from collections import deque

def solution(n, computers):
    answer = 0
    graph = {}
    for i in range(n):
        for j in range(n):
            if i not in graph:
                graph[i] = []

            if i != j and computers[i][j] == 1:
                graph[i].append(j)
        
    
    visited = {}
    def bfs(graph, start_v):
        q = deque()
        q.append(start_v)
        visited[start_v] = True
        while q:
            cur_v = q.popleft()
            for v in graph[cur_v]:
                if v not in visited:
                    visited[v] = True
                    q.append(v)    
        
    network = 0
    for i in graph:
        if i not in visited:
            bfs(graph, i)
            network += 1    
        
    return network