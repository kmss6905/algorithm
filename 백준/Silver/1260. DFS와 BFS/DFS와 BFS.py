from collections import deque


def bfs(graph, start, len):
    visited = [False] * (len + 1)
    q = deque()
    q.append(start)
    visited[start] = True
    answer = [start]
    while q:
        v = q.popleft()
        for nv in graph[v]:
            if not visited[nv]:
                visited[nv] = True
                q.append(nv)
                answer.append(nv)

    return answer


def dfs(cur_v):
    visited[cur_v] = True
    answer.append(cur_v)
    for next_v in graph[cur_v]:
        if not visited[next_v]:
            dfs(next_v)


def solutions():
    return 0


if __name__ == '__main__':
    N, M, start = map(int, input().split())
    graph = {}
    for i in range(1, N + 1):
        graph[i] = []

    for _ in range(M):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    for key in graph:
        graph[key].sort()

    visited = [False] * (N + 1)
    answer = []
    dfs(start)
    print(" ".join(map(str, answer)))
    print(" ".join(map(str, bfs(graph, start, N))))
