# 스테이지 별 도달한 수를 관리하는 해시 테이블 만들기
# 실패율 관리하는 리스트 만들기
# N 을 1부터 N+1 까지 반복하면서 실패율 계산하기
# 해시테이블에서 스테이지별 도달한 수 가져오기 / 적어도 i 번째 스테이지까지 도달한 플레이어수 누적합으로 계산 -> 만약 도달한 수가 0 이면 실패율 0
from collections import defaultdict

def solution(N, stages):
    answer = []
    table = defaultdict(int)
    for stage in stages:
        table[stage] += 1
    
    total_stage = len(stages)
    
    for i in range(1, N+1):
        if i not in table:
            answer.append((i, 0))
            continue
            
        answer.append((i, table[i] / total_stage))
        total_stage -= table[i]
    
    answer = [i[0] for i in sorted(answer, key=lambda x: x[1], reverse=True)]
    return answer