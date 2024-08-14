# 가로 9 -> -4, 4
# 세로 9 -> 4 위, -4 아래 9 - 1 // 2
def solution(keyinput, board):
    answer = []
    direction = {
        'left' : (-1, 0),
        'right': (1, 0),
        'up': (0, 1),
        'down': (0, -1)
    }
    lenx = (board[0]-1)// 2
    leny = (board[1]-1) // 2
    
    start = [0, 0]
    for key in keyinput:
        x, y = direction[key][0], direction[key][1]
        if abs(start[0]+x) > lenx:
            continue
        if abs(start[1]+y) > leny:
            continue
        start[0] += x
        start[1] += y
    
    return start