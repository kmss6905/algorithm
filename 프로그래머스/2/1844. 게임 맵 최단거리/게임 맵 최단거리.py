from collections import deque

# 방문을 언제하냐? 실제 visited 에 체크는 언제?
def solution(maps):
    answer = 0
    m = len(maps) # y
    n = len(maps[0]) # x
    visited = [[0] * n for _ in range(m)]
    print(visited)
    start = (0, 0)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    
    q = deque()
    q.append((1, 0, 0))
    visited[0][0] = 1
    while q:
        cnt, cy, cx = q.popleft()
        
        if cy == m-1 and cx == n-1:
            return cnt
        
        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]
            # 맵을 벗어나면 안되고, 벽이 아니고 방문하지 않은 곳이어야 한다.
            if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1:
                if visited[ny][nx] == 0: # 방문하지 않은 곳
                    visited[ny][nx] = cnt+1
                    q.append((cnt+1, ny, nx)) 
    
    return -1