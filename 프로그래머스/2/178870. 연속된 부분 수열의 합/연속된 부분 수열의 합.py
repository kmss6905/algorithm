# https://djgohigh.tistory.com/93
def solution(sequence, k):
    # 투포인터 각각 가리킬 왼,오 인덱스 선언
    l = r = 0
    
    # 최대 가장 긴 경우
    answer = [0, len(sequence)]
    sum = sequence[0]

    while True:
        # 합이 k 보다 작은 경우
        if sum < k:
            # 우측으로 이동하면서 누적합 구함
            r += 1
            if r == len(sequence): break
            sum += sequence[r]
        # 합이 k 보다 작거나 같은 경우
        else:
            if sum == k:
                # 배열의 원소 개수가 최소인 것만 추가한다.
                if r-l < answer[1]-answer[0]:
                    answer = [l, r]
            # sum >= k 무조건 sum 은 갱신되어야한다. 그렇게 해야 모든 경우 탐색 가능
            sum -= sequence[l]
            
            # 왼쪽에서 증가
            l += 1
    return answer