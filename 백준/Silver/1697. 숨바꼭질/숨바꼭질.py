from collections import deque

def solutions(N, K):
    answer = 0
    if N == K:
        return answer
    MAX = 100001
    visited = [0] * MAX
    visited[N] = True

    q = deque()
    q.append((0, N))

    while q:
        cnt, idx = q.popleft()

        if idx == K:
            answer = cnt
            break

        if 0 <= idx + 1 < MAX and not visited[idx + 1]:
            q.append((cnt + 1, idx + 1))
            visited[idx + 1] = True

        if 0 <= idx - 1 < MAX and not visited[idx - 1]:
            q.append((cnt + 1, idx - 1))
            visited[idx - 1] = True

        if 0 <= idx * 2 < MAX and not visited[idx * 2]:
            q.append((cnt + 1, idx * 2))
            visited[idx * 2] = True

    return answer


if __name__ == '__main__':
    N, K = map(int, input().split())
    print(solutions(N, K))
