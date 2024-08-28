import heapq

def dijkstra(start, n, graph):
    MAX = 100 * 1000
    dist = [MAX] * (n + 1)
    dist[start] = 0
    hq = []
    heapq.heappush(hq, (0, start))
    
    while hq:
        cur_cost, node = heapq.heappop(hq)
        
        if cur_cost > dist[node]:
            continue
        
        for next_node, next_cost in graph[node]:
            total_cost = cur_cost + next_cost
            if total_cost < dist[next_node]:
                dist[next_node] = total_cost
                heapq.heappush(hq, (total_cost, next_node))
    
    return dist

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
reverse_graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))
    reverse_graph[e].append((s, t))

# X번 마을에서 모든 마을로 가는 최단 거리
distance_from_x = dijkstra(x, n, graph)
# 모든 마을에서 X번 마을로 가는 최단 거리
distance_to_x = dijkstra(x, n, reverse_graph)

# 각 학생의 왕복 시간을 계산하고, 그 중 가장 긴 시간을 찾음
max_time = 0
for i in range(1, n + 1):
    max_time = max(max_time, distance_from_x[i] + distance_to_x[i])

print(max_time)