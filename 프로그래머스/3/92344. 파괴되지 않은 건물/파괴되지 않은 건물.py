def solution(board, skill):
    n = len(board)
    m = len(board[0])
    delta = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for sk in skill:
        degree = -sk[5] if sk[0] == 1 else sk[5]
        sr, sc, er, ec = sk[1], sk[2], sk[3], sk[4]
        
        delta[sr][sc] += degree # 경계가 겹칠 수 있다.(지워질 수 있음)
        delta[sr][ec + 1] += -degree
        delta[er + 1][sc] += -degree
        delta[er + 1][ec + 1] += degree
    
    # 열을 고정
    for c in range(m):
        # 행을 진행
        for r in range(1, n):
            delta[r][c] += delta[r-1][c]
    
    # 행을 고정
    for r in range(n):
        # 열을 진행
        for c in range(1, m):
            delta[r][c] += delta[r][c-1]
    
    answer = 0
    for r in range(n):
        for c in range(m):
            board[r][c] += delta[r][c]
            if board[r][c] > 0:
                answer += 1
                
    
    return answer
    

# def solution(board, skill):
#     # 남아있는 건물 수
#     answer = len(board) * len(board[0])
    
#     # 정확성 : m(10^2), 효율성 : m(대략, 2.5 * 10^5)
#     for l in skill:
#         start_x, start_y = l[1], l[2] # (1, 0)
#         end_x, end_y = l[3], l[4] # (3, 1)
#         score = l[5]
        
        
#         # 정확성 : m(10^4), 효율성 : m(10^6)
#         # 공격
#         if l[0] == 1:
#             for i in range(l[1], l[3]+1):
#                 for j in range(l[2], l[4]+1):
#                     # 건물이 존재하다가 파괴되는 경우
#                     if board[i][j] > 0 and board[i][j] - score <= 0:
#                         answer -= 1
#                     board[i][j] -= score
#         # 회복
#         else:
#             for i in range(l[1], l[3]+1):
#                 for j in range(l[2], l[4]+1):
#                     # 이미 파괴된 건물인데 복구되는 경우
#                     if board[i][j] <= 0 and board[i][j] + score > 0:
#                         answer += 1
#                     board[i][j] += score    
    
#     # 정확성에서는 m(10^6), 효율성 m(10^11 이상~)
#     return answer