from collections import deque

def solutions(M, N, K):
    graph = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for _ in range(K):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[y][x] = True
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            cx, cy = q.popleft()
            for dy, dx in directions:
                nx = cx + dx
                ny = cy + dy
                if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and \
                    graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    q.append((nx, ny))

    answer = 0
    for y in range(N):
        for x in range(M):
            if not visited[y][x] and graph[y][x] == 1:
                bfs(x, y)
                answer += 1
    return answer


if __name__ == '__main__':
    answer = []
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        answer.append(solutions(M, N, K))

    for i in answer:
        print(i)
