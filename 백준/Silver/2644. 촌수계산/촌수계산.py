from collections import deque

if __name__ == '__main__':
    n = int(input())
    visited = [False] * (n + 1)
    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    start, end = map(int, input().split())
    m = int(input())
    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    q = deque()
    q.append((0, start))
    visited[start] = True
    answer = -1
    while q:
        cnt, node = q.popleft()
        if node == end:
            # 도달 했을 때의 촌수 출력
            answer = cnt
            break

        for next_node in graph[node]:
            if not visited[next_node]:
                q.append((cnt + 1, next_node))
                visited[next_node] = True


    print(answer)