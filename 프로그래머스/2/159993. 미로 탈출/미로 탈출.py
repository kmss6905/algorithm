from collections import deque

def findDestinationByType(maps, _type):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == _type:
                return (i, j)
            
def bfs(srcx, srcy, src_cost, destinationType, maps):
    queue = deque()
    visited = [[-1] * len(maps[0]) for _ in range(len(maps))]
    distinations = [(-1,0), (1,0), (0, 1), (0, -1)]
    
    queue.append((srcx, srcy, src_cost))
    visited[srcx][srcy] = src_cost
    
    while queue:
        cx, cy, cost = queue.popleft()
        for dx, dy in distinations:
            nx = cx + dx
            ny = cy + dy
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and visited[nx][ny] == -1:
                if maps[nx][ny] == destinationType:
                    return (nx, ny, cost+1)
                
                if maps[nx][ny] != 'X' :
                    visited[nx][ny] = cost + 1
                    queue.append((nx, ny, cost+1))
    return (0,0,-1)
    
    

def solution(maps):
    x, y = findDestinationByType(maps, 'S')
    lever_x, lever_y, lever_cost = bfs(x, y, 0, 'L', maps)
    if lever_cost == -1:
        return -1
    exit_x, exit_y, exit_cost = bfs(lever_x, lever_y, lever_cost, 'E', maps)
    return exit_cost
                    
    
    
                  