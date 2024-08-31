import heapq

def solution(n, s, a, b, fares):
    # 그래프 초기화
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
    
    # 다익스트라 알고리즘 함수 정의
    def dijkstra(start, graph):
        MAX = 1000000 * n
        dist = [MAX] * (n+1)
        dist[start] = 0
        hq = [(0, start)]
        
        while hq:
            cur_cost, cur_node = heapq.heappop(hq)
            
            if dist[cur_node] < cur_cost:
                continue
                   
            for next_cost, next_node in graph[cur_node]:
                total_cost = next_cost + cur_cost
                if total_cost < dist[next_node]:
                    dist[next_node] = total_cost
                    heapq.heappush(hq, (total_cost, next_node))
        return dist
    
    # s, a, b에서 각각 다익스트라 실행
    dist_s = dijkstra(s, graph)
    dist_a = dijkstra(a, graph)
    dist_b = dijkstra(b, graph)
    
    # 최소 비용 계산
    answer = float('inf')
    for i in range(1, n+1):
        answer = min(answer, dist_s[i] + dist_a[i] + dist_b[i])
    
    return answer
