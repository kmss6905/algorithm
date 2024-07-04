'''
최대 n은 100개 -> 생길 수 있는 wires 수는 최대 99개
100 * 100 => 10^4 -> 완탐으로해도 가능!

1. 하나씩 wires 를 없애보면서 각 노드의 수를 새어보고 차이를 계산한다.

'''
from collections import deque

def solution(n, wires):
    differs = []
    for i in range(len(wires)):
        new_list = wires[:i] + wires[i+1:]
        graph = {}
        for x, y in new_list:
            if x not in graph:
                graph[x] = []
            if y not in graph:
                graph[y] = []
            graph[x].append(y)
            graph[y].append(x)
        
        print(new_list, graph)
        visited = {node: False for node in graph}
        islands = []
        
        def bfs(graph, node):
            visited[node] = True
            cv = 1
            queue = deque([node])
            while queue:
                current_node = queue.popleft()
                for next_node in graph[current_node]:
                    if visited[next_node] == False:
                        visited[next_node] = True
                        queue.append(next_node)
                        cv += 1
            return cv
    
        for node in graph:
            if not visited[node]:
                island_size = bfs(graph, node)
                islands.append(island_size)

        if len(islands) == 1:
            differs.append(islands[0] - 1) # 1개만 있다는 건, 노드 하나인 섬이 존재한다는 뜻 따라서 1 빼줘야함
        else:
            differs.append(abs(islands[0]-islands[1]))
    return min(differs)