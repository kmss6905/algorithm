"""
3차원 어떻게 입력을 받아야 할 지 바로 머리 속으로 떠오르지 않는다.

BFS
visited = [[False] * m for _ in range(n)] * h

for i in range(h):
    for j in range(n):
        for k in range(m):


for i in range(h):
    for j in range(n):
        graph[i][j] = list(map(int, input().split()))


"""
from collections import deque

def solutions():
    m, n, h = map(int, input().split())
    visited = [[[False] * m for _ in range(n)] for _ in range(h)]
    graph = [[[] * m for _ in range(n)] for _ in range(h)]

    for i in range(h):
        for j in range(n):
            graph[i][j] = list(map(int, input().split()))

    starts = []
    # 토마토 찾기 + visited 체크
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 1:
                    starts.append((0, x, y, z))

    def bfs():
        q = deque()
        for i in starts:
            q.append(i)

        for day, x, y, z in starts:
            visited[z][y][x] = True

        directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        min_day = -1
        while q:
            day, x, y, z = q.popleft()
            min_day = day
            for dx, dy, dz in directions:
                next_x = x + dx
                next_y = y + dy
                next_z = z + dz
                # 인덱스
                if 0 <= next_x < m and 0 <= next_y < n and 0 <= next_z < h and graph[next_z][next_y][next_x] == 0 and not visited[next_z][next_y][next_x]:
                    graph[next_z][next_y][next_x] = 1  # 토마토 갱신
                    q.append((day+1, next_x, next_y, next_z))
                    visited[next_z][next_y][next_x] = True
        return min_day
    
    md = bfs()
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:
                    return -1

    return md


if __name__ == '__main__':
    print(solutions())
