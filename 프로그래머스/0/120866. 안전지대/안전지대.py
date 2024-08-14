def solution(board):
    answer = 0
    n = len(board[0])
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1 ,-1), (-1, 1), (1, -1), (1, 1)]
    for i in range(n):
        for j in range(n):
            # 지뢰 매설 지역
            if board[i][j] == 1:
                for row, col in direction:
                    if 0 <= i+row < n and 0 <= j+col < n:
                        if board[i+row][j+col] == 0:
                            board[i+row][j+col] = -1
                        
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                answer += 1
    
    return answer