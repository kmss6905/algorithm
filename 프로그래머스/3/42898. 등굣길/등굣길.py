def solution(m, n, puddles):
    # dp 테이블 초기화
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    # 웅덩이 좌표 변환
    puddles = [[y, x] for [x, y] in puddles]
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue  # 시작점은 이미 처리됨
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[n][m] % 1000000007
