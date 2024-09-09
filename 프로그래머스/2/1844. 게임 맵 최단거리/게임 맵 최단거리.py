from collections import deque

def solution(maps):
    row = len(maps) # 행
    col = len(maps[0]) # 열
    
    # 방문 여부를 저장할 2차원 배열
    visited = [[-1] * col for _ in range(row)]
    
    # 상하좌우 방향 이동을 위한 리스트
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 시작점을 큐에 넣고 방문 여부를 체크
    queue = deque([(0, 0)])
    visited[0][0] = 1
    
    while queue:
        y, x = queue.popleft()
        distance = visited[y][x] # 현재 위치까지의 거리
        
        # 상하좌우 이동을 확인하며 탐색
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            
            # 맵을 벗어나지 않고, 이동 가능한 칸이며, 방문하지 않은 경우
            if 0 <= ny < row and 0 <= nx < col and maps[ny][nx] == 1 and visited[ny][nx] == -1:
                visited[ny][nx] = distance + 1 # 거리 갱신
                queue.append((ny, nx)) # 큐에 새로운 위치 추가
                if ny == row - 1 and nx == col - 1:
                    return visited[ny][nx]
    
    # 상대 팀 진영에 도착할 수 없는 경우
    return -1