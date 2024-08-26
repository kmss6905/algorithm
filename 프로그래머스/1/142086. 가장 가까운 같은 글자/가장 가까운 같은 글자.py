def solution(s):
    answer = []
    memo = {}
    for idx, e in enumerate(list(s)):
        if e not in memo:
            memo[e] = idx
            answer.append(-1)
            continue
        # 가장 가까운 곳에 있는 글자와 얼마나 떨어져있는 지 계산
        distance = idx - memo[e]
        answer.append(distance)
        
        # e 글자가 몇번 째 인덱스에 마지막으로 등장했는 지를 기록
        memo[e] = idx
        
    return answer