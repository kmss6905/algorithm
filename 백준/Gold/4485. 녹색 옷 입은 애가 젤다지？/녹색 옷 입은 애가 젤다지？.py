import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]  # 상하좌우
dy = [0, 0, -1, 1]

def dijkstra(graph, n):
    dist = [[INF] * n for _ in range(n)]
    dist[0][0] = graph[0][0]
    pq = [(graph[0][0], 0, 0)]  # (비용, x, y)
    
    while pq:
        current_dist, x, y = heapq.heappop(pq)
        
        if x == n - 1 and y == n - 1:  # 목적지에 도달한 경우
            return current_dist
        
        if dist[x][y] < current_dist:
            continue
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < n:
                new_dist = current_dist + graph[nx][ny]
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heapq.heappush(pq, (new_dist, nx, ny))

k = 1
while True:
    n = int(input())
    if n == 0:
        exit()
    
    graph = [list(map(int, input().split())) for _ in range(n)]
    result = dijkstra(graph, n)
    print(f"Problem {k}: {result}")
    k += 1 
