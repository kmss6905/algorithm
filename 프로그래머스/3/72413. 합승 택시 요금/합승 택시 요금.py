import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
    
    def dijkstra(start):
        MAX = 100000 * 200
        dist = [MAX] * (n+1)
        dist[start] = 0
        
        hq = []
        heapq.heappush(hq, (0, start))
        
        visited = [False] * (n+1)
        while hq:
            cur_cost, cur_node = heapq.heappop(hq)
            
            if dist[cur_node] < cur_cost:
                continue
            
            for next_cost, next_node in graph[cur_node]:
                total_cost = cur_cost + next_cost
                if total_cost < dist[next_node]:
                    dist[next_node] = total_cost
                    heapq.heappush(hq, (total_cost, next_node))
        return dist
    
    distance = dijkstra(s)
    res = distance[a] + distance[b]
    for i in range(1, n+1):
        if i == s:
            continue
        point_dist = dijkstra(i)
        res = min(point_dist[a]+point_dist[b]+distance[i], res)
    return res