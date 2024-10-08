"""
종류 별로 옷의 개수를 해시테이블에 저장한 후
모든 옷 개수를 곱한 결과에서 1뺀다.
어차피 30개 이하이기 때문에 시간복잡도 굳이 고려할 필요는 없다.
clothes 의 길이 30

"""
def solution(clothes):
    answer = 1
    clothes_map = {}
    for cloth, cloth_type in clothes:
        if cloth_type not in clothes_map:
            clothes_map[cloth_type] = 2
        else:
            clothes_map[cloth_type] += 1
    
    for value in clothes_map.values():
        answer *= value
    answer -= 1
    return answer