"""
1. 아이디어
2. 시간복잡도
3. 구현
"""
def solution(sequence):
    answer = 0
    se1 = [sequence[i] if i % 2 == 0 else -1 * sequence[i] for i in range(len(sequence))]
    se2 = [-1 * sequence[i] if i % 2 == 0 else sequence[i] for i in range(len(sequence))]
    
    dp1, dp2 = [0] * len(sequence), [0] * len(sequence)
    dp1[0], dp2[0] = 0, 0
    
    # dp[i], i 번째 수 까지 가질 수 있는 연속 철스 수열의 최대 합
    for i in range(1, len(sequence)):
        dp1[i] = max(se1[i], se1[i] + dp1[i-1])
        dp2[i] = max(se2[i], se2[i] + dp2[i-1])
    
    ans = max(max(dp1), max(dp2))
    return ans