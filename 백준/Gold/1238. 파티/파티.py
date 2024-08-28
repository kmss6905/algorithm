# 그래프, 최단시간 -> 다익스트라

# 그래프 구현 graph = [[] for _ in range(n+1)]
# 입력값 시작마을, 종료마을 받고 리턴값으로 종료마을에 도달했을 경우의 비용 함수 만들기
# 모든 마을을 돌면서 왕복 비용 계산해서 가장 최대값을 res 에 넣으면서 갱신
import heapq
    
    
def dilkstra(start, end, n, graph):
    if start == end:
        return 0
    MAX = 100 * 1000
    dist = [MAX] * (n+1)
    dist[start] = 0
    hq = []
    visited = [False] * (n+1)
    heapq.heappush(hq, (0, start))
    while hq:
        cur_cost, node = heapq.heappop(hq)
        if visited[node]:
            continue
        visited[node] = True
        for next_cost, next_node in graph[node]:
            total_cost = next_cost + cur_cost
            if total_cost < dist[next_node]:
                dist[next_node] = total_cost
                heapq.heappush(hq, (total_cost, next_node))
        
    return dist[end]
        
        
n,m,x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((t, e))

res = 0
for start in range(1, n+1):
    res = max(res, dilkstra(start, x, n, graph) + dilkstra(x, start, n, graph))
    
print(res)
