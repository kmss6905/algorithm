def solution(k, m, score):
    answer = 0
    score = sorted(score, reverse=True)
    ac = 0
    mac = 9
    for i in range(len(score)):
        ac += 1
        mac = min(mac, score[i])
        if ac == m:
            answer += (mac * m)
            ac = 0
            mac = 9
        
    return answer