def solution(sequence):
    # 두 가지 형태의 펄스 수열을 생성
    arr1 = [sequence[i] if i % 2 == 0 else -sequence[i] for i in range(len(sequence))]
    arr2 = [-sequence[i] if i % 2 == 0 else sequence[i] for i in range(len(sequence))]
    
    # dp 배열 초기화: dp1과 dp2는 각각 arr1, arr2에서의 최대 부분합을 저장
    dp1, dp2 = [0] * len(sequence), [0] * len(sequence)
    dp1[0], dp2[0] = arr1[0], arr2[0]  # 첫 번째 값으로 초기화
    
    # i 번째 수까지의 최대 펄스 수열 합을 계산
    for i in range(1, len(sequence)):
        dp1[i] = max(arr1[i], arr1[i] + dp1[i-1])
        dp2[i] = max(arr2[i], arr2[i] + dp2[i-1])
    
    # 두 펄스 수열 중 최대값 반환
    ans = max(max(dp1), max(dp2))
    return ans
