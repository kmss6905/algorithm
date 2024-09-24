"""
문제를 해석하는 데 왤케 시간이 걸리는 거지?.. 문해력이 딸리나?

아이디어: 빡 구현, BFS ? x
구현:

기능을 나누자.
1. 현재 위치에서 i 포인트 번째 까지 가는 경로 좌표(r, c 룰 적용)
2. 가장 경로가 긴 로봇 기준으로 for 문 돌면서 겹치는 위치가 있는 지 확인하기

시간복잡도
1. 하나의 로봇이 모든 경로를 이동할 때 시간복잡도 : 100 * 100 = 10000 (max)
2  총 로봇 수 = 100개
100 * 100 * 100 => 10^6

가장 긴 경로를 움직인 로봇 기준 ( 최대 100 ) 으로 반복
O(N)

총 시간복잡도 = O(N^3) + O(N)
따라서 O(N^3)

수두코드
point.insert(0, [0, 0])
robot_routes = []

# 굳이 -1 하는 등의 과정을 하지 않도록 바꾸자.
for i in range(len(routes)):
    rs = [routes[i][0]]
    
    
    routes[i][1] ... routes[i][len(routes[i]) - 1]
    
    
    

(현재좌표, 그 다음 포인트)
현재 좌표에서 다음 포인트 도달할 때 까지 좌표 저장


"""
# [3,2], [4,7]
def to(start, end):
    # 항상 y 가 먼저 이동
    sy, sx = start
    ey, ex = end
    answer = []
    while sx != ex or sy != ey:
        if sy != ey:
            if sy > ey:
                sy -= 1
            if sy < ey:
                sy += 1
            answer.append([sy, sx])
            continue

        if sx != ex:
            if sx > ex:
                sx -= 1
            if sx < ex:
                sx += 1
            answer.append([sy, sx])
            continue

    return answer



def solution(points, routes):
    answer = []
    points.insert(0, [0, 0])
    robot_routes = [[] for _ in range(len(routes))]

    mlr = -1
    for i in range(len(routes)):
        rs = []
        for j in range(len(routes[i])):
            if j == 0: # 시작점인 경우
                rs.append(points[routes[i][j]])
                continue
            rs += to(rs[-1], points[routes[i][j]]) # 가장 최근까지 간 point 에서 다음에 가려고 하는 point 까지 가는 모든 경로
        robot_routes[i] = rs
        mlr = max(mlr, len(rs))

    # debug 각 로봇이 이동한 경로들
    # for i in range(len(robot_routes)):
    #     print(i, robot_routes[i])

    # 가장 긴 것 기준으로 본다
    cnt = 0
    for time in range(mlr):
        answer = {}  # 각 시간에 좌표가 몇 번 등장했는지 기록하는 딕셔너리
        for i in range(len(robot_routes)):
            if len(robot_routes[i]) <= time:
                continue  # 해당 시간에 로봇이 아직 움직이지 않았다면 건너뜀

            pos_tuple = (robot_routes[i][time][0], robot_routes[i][time][1])
            
            if pos_tuple not in answer:
                answer[pos_tuple] = 1
            else:
                answer[pos_tuple] += 1
        
    
        for value in answer.values():
            if value >= 2:
                cnt += 1
    return cnt

