from collections import deque

def solutions():
    m, n, h = map(int, input().split())
    visited = [[[False] * m for _ in range(n)] for _ in range(h)]
    graph = []

    for _ in range(h):
        layer = [list(map(int, input().split())) for _ in range(n)]
        graph.append(layer)

    # 토마토 위치 찾기
    starts = [(0, x, y, z) for z in range(h) for y in range(n) for x in range(m) if graph[z][y][x] == 1]

    def bfs():
        q = deque(starts)
        directions = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
        min_day = -1

        # BFS 탐색
        while q:
            day, x, y, z = q.popleft()
            min_day = day

            for dx, dy, dz in directions:
                nx, ny, nz = x + dx, y + dy, z + dz

                # 인덱스 범위 및 토마토 상태 체크
                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and graph[nz][ny][nx] == 0 and not visited[nz][ny][nx]:
                    graph[nz][ny][nx] = 1
                    visited[nz][ny][nx] = True
                    q.append((day+1, nx, ny, nz))

        return min_day

    # BFS 실행
    md = bfs()

    # 익지 않은 토마토가 있는지 확인
    if any(graph[z][y][x] == 0 for z in range(h) for y in range(n) for x in range(m)):
        return -1

    return md

if __name__ == '__main__':
    print(solutions())
