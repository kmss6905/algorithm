def solution(targets):
    answer = 0
    cnt = 0
    attack_position = 0
    targets.sort(key = lambda x :x[1])
    for start, end in targets:
        if attack_position <= start:
            attack_position = end
            print(attack_position)
            cnt += 1
    return cnt