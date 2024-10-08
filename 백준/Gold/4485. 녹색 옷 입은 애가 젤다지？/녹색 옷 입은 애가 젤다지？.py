"""
1. 아이디어
가중치가 있는 그래프에서 최소 비용으로 목적지 도착하기 -> 우선순위 큐 -> 힙 자료구조

2. 구현
그래프 구현
단, 0 이 입력 될때까지 계속해서 입력 받음
각 지점 별 비용과 노드 위치를 힙 자료구조에 push 한다.
이때 마지막에 도착했을 때의 비용 계산
비용그래프는 costs

3. 시간복잡도
한 vertex 당 연결된 노드의 수를 계산 해보면 최대 4개이다.
전체 n ^ 2 개의 vertex

4 *  n^2
최대 n =  5 ^ 4 => 125 -> 10^2 보다는 크고 10^3 보다는 작다
heap 크기 10^5
4번씩 일어난다. 따라서

노드의 수 : V
엣지(간선)의 수 : E
우선순위 큐(힙)의 연산 : 힙의 삽입과 삭제는 O(logV)

노드의 수 n^2
엣지의 수는 각 노드마다 4방향 -> 4 * n^2
4 * n^2 * log(n^2)

"""
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
cnt = 1


def solutions(graph, n):
    costs = [[INF] * n for _ in range(n)]
    costs[0][0] = graph[0][0]
    hq = [(costs[0][0], 0, 0)] # (비용, x, y)

    while hq:
        cur_cost, y, x = heapq.heappop(hq)

        # 젤다에 도달
        if y == n - 1 and x == n - 1:
            return cur_cost

        if costs[y][x] < cur_cost:
            continue

        for dy, dx in directions:
            next_y = y + dy
            next_x = x + dx
            if 0 <= next_x < n and 0 <= next_y < n:
                next_cost = cur_cost + graph[next_y][next_x]
                if next_cost < costs[next_y][next_x]:
                    costs[next_y][next_x] = next_cost
                    heapq.heappush(hq, (next_cost, next_y, next_x))
    return costs[n - 1][n - 1]


while True:
    n = int(input())
    if n == 0:
        exit()

    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = solutions(graph, n)
    print(f"Problem {cnt}: {answer}")
    cnt += 1

