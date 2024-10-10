"""
문제를 해석하는 데 왤케 시간이 걸리는 거지?.. 문해력이 딸리나?

아이디어: 빡 구현, BFS ? x
구현:

기능을 나누자.
1. 현재 위치에서 i 포인트 번째 까지 가는 경로 좌표(r, c 룰 적용)
2. 가장 경로가 긴 로봇 기준으로 for 문 돌면서 겹치는 위치가 있는 지 확인하기

시간복잡도
1. 하나의 로봇이 모든 경로를 이동할 때 시간복잡도 : 100 + 100 ( 특수한 이동 조건 때문임 )
2  총 로봇 수 = 100개
200 * 100 => 2만

(N + N) * N  => 2N * N => 2 * N^2

수두코드
point.insert(0, [0, 0])
robot_routes = []

# 굳이 -1 하는 등의 과정을 하지 않도록 바꾸자.
for i in range(len(routes)):
    rs = [routes[i][0]]
    
    
    routes[i][1] ... routes[i][len(routes[i]) - 1]
    
    

풀이 해설
rotues = [[4, 2], [1, 3], [2, 4]]
[4, 2] -> 1번째 로봇이 4번 포인트에서 출발에서 2번까지 가야하는 경로를 표현

아이디어 1)
모든 로봇이 출발지점에서 끝지점까지는 경로를 모두 구해둔다.
1 -> []
2 -> []
3 -> []
가장 긴 경로의 로봇 길이 구한 후 해당 길이를 기준으로 i 번쨰 같은 것이 있는 지 확인하기
따라서 중요한 것은 현재 이동하고 있는 좌표를 반.드.시 저장해야한다.
중요한 건 BFS 처럼 보이지만, y 좌표가 반드시 먼저 이동하고 그 이후 x 좌표를 이동하며 최단경로를 가야하기 때문에 deque 를 굳이 사용하지 않아도 된다.

(현재좌표, 그 다음 포인트)
현재 좌표에서 다음 포인트 도달할 때 까지 좌표 저장

"""
# [3,2], [4,7]
def to(start, end):
    # 항상 y 가 먼저 이동
    sy, sx = start
    ey, ex = end
    answer = []
    while sy != ey or sx != ex:
        if sy != ey:
            sy += 1 if sy < ey else -1
        elif sx != ex:
            sx += 1 if sx < ex else -1
        answer.append([sy, sx])
    return answer


def solution(points, routes):
    points.insert(0, [0, 0])
    robot_routes = [[] for _ in range(len(routes))]

    max_length = -1
    for i in range(len(routes)):
        # i 번째 로봇 경로 저장
        rs = []
        for j in range(len(routes[i])):
            if j == 0: # 시작점인 경우
                rs.append(points[routes[i][j]])
                continue
            rs += to(rs[-1], points[routes[i][j]]) # 가장 최근까지 간 point 에서 다음에 가려고 하는 point 까지 가는 모든 경로
        robot_routes[i] = rs
        max_length = max(max_length, len(rs))

    # debug 각 로봇이 이동한 경로들
    # for i in range(len(robot_routes)):
    #     print(i, robot_routes[i])

    # 가장 긴 것 기준으로 본다
    cnt = 0
    for time in range(max_length):
        # 각 시간에 좌표가 몇 번 등장했는지 기록하는 딕셔너리
        # 키를 좌표로 잡고, 
        answer = {}
        for i in range(len(robot_routes)):
            if len(robot_routes[i]) <= time:
                continue  # 해당 시간에 로봇이 아직 움직이지 않았다면 건너뜀

            
            pos_tuple = (robot_routes[i][time][0], robot_routes[i][time][1])
            # answer[pos_tuple] = answer.get(pos_tuple, 0) + 1
            if pos_tuple not in answer:
                answer[pos_tuple] = 1
            else:
                answer[pos_tuple] += 1
            
        # 겹쳤던 경로들을 조회한다.
        for value in answer.values():
            # value = 2 라는 것은 최소 겹쳤다는 말과 같다.
            if value >= 2:
                cnt += 1
    return cnt

