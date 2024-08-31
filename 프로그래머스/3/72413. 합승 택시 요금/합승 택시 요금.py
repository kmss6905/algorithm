"""
그래프
출발지와 graph 를 받는다.

s 시작 다익 200 log200
a 시작 다익 200 log200
b 시작 다익 200 log200

"""
import heapq

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    for c, d, f in fares:
        graph[c].append((f, d))
        graph[d].append((f, c))
    
    def dijkstra(start, graph):
        MAX = 1000000 * n
        dist = [MAX] * (n+1)
        hq = []
        heapq.heappush(hq, (0, start))
        
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
    
    # s -> a, s -> b
    fs = dijkstra(s, graph)
    answer = fs[a] + fs[b]
    
    from_a = dijkstra(a, graph)
    from_b = dijkstra(b, graph)
    
    print(from_a)
    print(from_b)
    print(answer)
    for i in range(1, n+1):
        if i == s:
            continue
            
        answer = min(answer, fs[i] + from_a[i] + from_b[i])

    return answer
                     
                     
                     
                     
                     
                     
                     