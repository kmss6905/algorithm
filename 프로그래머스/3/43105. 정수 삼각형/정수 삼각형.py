"""
triangle 의 비용 테이블을 만든다. -> 어떻게? triangle 밑변 길이의 최대값 기준으로 2차 배열 만든다.
triangle 을 탐색 하면서 비용테이블을 업데이트 한다.
이전에 사용했던 비용을 참고하여 업데이트 한다.
총 3가지로 분류한다.
1. 좌변, 우변, 나머지에 있는 원소
좌변의 현재 비용은 바로 위 현재까지의 좌변 원소 비용와 현재 원소 비용 더함
우변의 현재 비용은 바로 위 현재까지의 우변 원소 비용과 현재 원소 비용을 더함
올 수 있는 경우의 수는 바로 위칸 dp[i-1][j-1], dp[i+1][j] 중에 최대값 + 현재 원소 값을 dp 테이블에 업데이트
다 끝났을 때 마지막에 있는 원소 중 최대 값이 전체 비용 최대 값
           00
         10 11
        20 21 22
         01 -> 00
         22 -> 
"""
def solution(triangle):
    answer = 0 
    # 삼각형이 1, 2 인경우
    if len(triangle) == 1:
        return triangle[0][0]
    
    if len(triangle) == 2:
        return max(triangle[0][0] + triangle[1][0], triangle[0][0] + triangle[1][1])
    
    
    dp = [[0] * len(triangle[-1]) for _ in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    dp[1][0] = triangle[0][0] + triangle[1][0]
    dp[1][1] = triangle[0][0] + triangle[1][1]
    
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                dp[i][j] = triangle[0][0]
                continue
            
            # 좌
            if j == 0:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
                continue
            if j == (len(triangle[i]) - 1):
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                continue
            
            # 나머지
            dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    return max(dp[-1])