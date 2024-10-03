# https://velog.io/@alsry922/PCCP-%EA%B8%B0%EC%B6%9C%EB%AC%B8%EC%A0%9C-3%EB%B2%88-%EC%95%84%EB%82%A0%EB%A1%9C%EA%B7%B8-%EC%8B%9C%EA%B3%84 (참고한 풀이..)
def solution(h1, m1, s1, h2, m2, s2):
    answer = 0

    # 시작시간과 종료시간을 초단위로 계산한다.
    startTime = h1 * 3600 + m1 * 60 + s1
    endTime = h2 * 3600 + m2 * 60 + s2  

    # 시작 시간이 12시 인 경우 -> 시분침 다 겹침
    if startTime == 0 * 3600 or startTime == 12 * 3600: # m1, s1 모두 0이다.
        answer += 1

    while startTime < endTime:
        # 시침 1시간 = 30도 -> 1초에 30/3600도 즉, 1/120도 이동
        # 분침 1분 = 6도 -> 1초에 6/60도 즉, 1/10도 이동
        # 초침 1초 = 6도 -> 1초에 6도 이동
        # 현재 시,분,침의 각도
        hCurAngle = startTime / 120 % 360
        mCurAngle = startTime / 10 % 360
        sCurAngle = startTime * 6 % 360

        
        hNextAngle = 360 if (startTime + 1) / 120 % 360 == 0 else (startTime + 1) / 120 % 360
        mNextAngle = 360 if (startTime + 1) / 10 % 360 == 0 else (startTime + 1) / 10 % 360
        sNextAngle = 360 if (startTime + 1) * 6 % 360 == 0 else (startTime + 1) * 6 % 360

        # 각도가 정확해질 수는 없다는 것이 중요함. 시침이 1초동안 이동하는 각도 = 0.008333333 도
        # 1초 사이에 지나갈 수도 있기 때문에 아래과 같은 수식으로 작성해야함.
        if sCurAngle < hCurAngle and sNextAngle >= hNextAngle:
            answer += 1
        if sCurAngle < mCurAngle and sNextAngle >= mNextAngle:
            answer += 1
        # 시침/분침과 동시에 겹쳤을 때 중복카운팅 제외 (continue 로 하지 않고 이렇게 하는 것도 좋아 보인다!)
        if sNextAngle == hNextAngle and hNextAngle == mNextAngle:
            answer -= 1

        startTime += 1
    
    return answer

# """
# 각도로 계산하지 않고 루프를 빠져나오는 것은 초계산으로 통일하자.
# 1씩 증가한다.


# """
# def solution(h1, m1, s1, h2, m2, s2):
#     answer = -1
#     # 1초에 이동하는 각도 계산
#     per_sec_s = 6 # 6
#     per_sec_m = 360 / (60 * 60) # 0.1
#     per_sec_h = 360 / (60 * 60 * 12) # 0.008333333333333333
    
#     # 최초 각도
#     before = [per_sec_s * s1, per_sec_m * (m1 * 60), per_sec_h * (h1 * 60 * 60)]

    
#     answer = 0
#     while True:
#         if h1 == h2 and m2 == m2 and s1 == s2:
#             break
        
#         s1 += 1
#         if s1 == 60:
#             s1 = 0
#             m1 += 1
#             if m1 == 60:
#                 m1 = 0
#                 h1 += 1
#                 if h1 == 12:
#                     h1 = 0
        
#         # 초침 각이 분침 각도와 시침 각도와 완전히 같아지는 경우
#         current_sec_angel = per_sec_s * s1
#         current_min_angel = per_sec_m * (m1 * 60)
#         current_hour_angel = per_sec_h * (h1 * 60 * 60)
        
#         if current_sec_angel == current_hour_angel and current_sec_angel == current_min_angel:
#             answer += 1
#             continue
        
        
#         # 초침이 분침을 넘어가거나(이전 분침각도와 비교) 같아지는 경우
#         if before[0] < before[1] and current_sec_angel > current_min_angel:
#             answer += 1
#             continue
        
#         # 초침이 시침을 넘어가거나 같아지는 경우
#         if before[0] < before[2] and current_sec_angel > current_hour_angel:
#             answer += 1
#             continue
        
#         before[0] = current_sec_angel
#         before[1] = current_min_angel
#         before[2] = current_hour_angel
    
#     return answer