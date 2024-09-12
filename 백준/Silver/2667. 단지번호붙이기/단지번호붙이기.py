"""
아이디어 : bfs

그래프 구현, visited 구현

단지 수 -> bfs() 끝날때 마다 danji += 1
bfs 리턴 값 -> 탐색한 집 개수
    bfs 함수 내부에 탐색한 집의 개수를 새는 변수 house_cnt = 0 둠
    bfs 탐색 시에 카운팅한다

그리고 단지별 탐색한 집의 개수를 저장하는 배열 선언

시간 복잡도 : O(n^2) -> 25 * 25 -> 5^4
"""
from collections import deque

def solutions():
    N = int(input())
    graph = []
    visited = [[False] * N for _ in range(N)]
    for _ in range(N):
        a = list(map(int, input()))
        graph.append(a)

    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    def bfs(x, y):
        q = deque()
        q.append((0, x, y))
        visited[y][x] = True
        house_cnt = 1
        while q:
            cnt, x, y = q.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] == 1:
                    q.append((cnt + 1, nx, ny))
                    visited[ny][nx] = True
                    house_cnt += 1

        return house_cnt

    danji_cnt = 0
    house_cnts = []
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and graph[y][x] == 1:
                house_cnts.append(bfs(x, y))
                danji_cnt += 1

    print(danji_cnt)
    for cnt in sorted(house_cnts):
        print(cnt)



if __name__ == '__main__':
    solutions()
