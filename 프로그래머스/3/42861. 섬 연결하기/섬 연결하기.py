# from collections import deque

# def solution(n, costs):
#     answer = 0
#     graph = {}
#     for i in costs:
#         v1, v2, cost = i[0], i[1], i[2]
#         if v1 not in graph:
#             graph[v1] = []
#             graph[v1].append((cost,v2))
#         else:
#             graph[v1].append((cost,v2))

#         if v2 not in graph:
#             graph[v2] = []
#             graph[v2].append((cost, v2))
#         else:
#             graph[v2].append((cost, v2))
    
    
#     # 입력 받는 것 -> graph 
#     print(graph)
    
#     # 시작, 시작 vertex
#     start_node = costs[0][0]
    
#     sum = 0
    
#     visited = set()
#     visited.add(start_node)
#     q = deque()
#     q.append((0, start_node)) 
#     while q:
#         cur_cost, cur_node = q.popleft()
#         print(cur_cost, cur_node)
#         next_cost, next_node = min(sorted(graph[cur_node]))
#         print(next_cost, next_node)
#         if next_node not in visited:
#             sum += next_cost
#             visited.add(next_node)
#             print(visited)
#             q.append((sum, next_node))
#             if len(visited) == n:
#                 break
                
                
        
    
    
#     print(sum)
#     return answer

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x:x[2]) # 비용을 기준으로 오름차순 정렬
    print(costs)
    connect = set([costs[0][0]]) # 간선 연결 정보를 담는 set
    print(connect)
    while len(connect) != n:
        for cost in costs:
            node, node1, cc = cost[0], cost[1], cost[2]
            if node in connect and node1 in connect: # 사이클 형성을 막음
                continue
            if node in connect or node1 in connect: # 기존 간선과 이어져야 함
                connect.update([node, node1])
                answer += cc
                break
                
    return answer