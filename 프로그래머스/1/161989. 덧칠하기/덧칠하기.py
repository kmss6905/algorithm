def solution(n, m, section):
    answer = 0
    last_section = 0
    for empty in section:
        # 이미 칠한 경우에는 칠하지 않음
        if empty <= last_section:
            continue
        # 칠하기
        last_section = empty + (m-1)
        answer += 1
    return answer