"""
이중리스트로 주어진 plans 를 시간을 기준으로 오름차순 정렬한다.
"""
def time_to_minute(time_str):
    hour, minute = map(int, time_str.split(':'))
    return hour * 60 + minute

def solution(plans):
    answer = []
    stack = []
    pop_in_stack = False
    
    # 1. 과제 시작시간대로 오름차순 정렬과 동시에 시작시간->분으로 변경
    for i in range(len(plans)):
        plans[i][1] = time_to_minute(plans[i][1])
        plans[i][2] = int(plans[i][2])
    plans = sorted(plans, key=lambda x:x[1])
    print(plans)
    
    # 2. 과제 진행
    for i in range(len(plans)):
        now_sub, now_start, now_playtime = plans[i]
        # 마지막 과제면 바로 종료
        if i == len(plans) - 1:
            answer.append(now_sub)
            break
        next_sub, next_start, next_playtime = plans[i+1]
        playable_time = next_start - now_start
        # 다음 과제 시작 시간까지 다 끝내지 못했을 경우
        if now_playtime - playable_time > 0:
            stack.append((now_sub, now_playtime - playable_time))
        # 과제를 다 끝냈을 경우
        else:
            answer.append(now_sub)
            
            time = playable_time - now_playtime
            # 60
            # 멈춘 과제 업데이트
            if len(stack) != 0:
                while stack:
                    # 40
                    sub, curtime = stack.pop()
                    if time - curtime >= 0:
                        time -= curtime
                        answer.append(sub)
                        continue
                    
                    stack.append((sub, curtime - time))
                    break
                    
                
            
    
    # 3. 남은 과제 끝내기
    if len(stack) == 0:
        return answer
    
    while stack:
        answer.append(stack.pop()[0])
    return answer