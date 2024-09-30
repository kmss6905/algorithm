def solution(clothes):
    # 옷의 종류별 옷 개수
    clothes_map = {}
    for clothe in clothes:
        if clothe[1] not in clothes_map:
            clothes_map[clothe[1]] = 1
        else:
            clothes_map[clothe[1]] += 1
    result = 1
    for k in clothes_map:
        result *= (clothes_map[k] + 1)
    
    answer = result - 1
    return answer