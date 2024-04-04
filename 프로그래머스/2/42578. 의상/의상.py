from itertools import combinations
# def solution(clothes):
#     clothes_hm = {}
#     clothes_types = []
#     # 옷 종류 별로 입을 수 있는 옷을 나누기
#     for i in clothes:
#         if i[1] not in clothes_hm:
#             clothes_hm[i[1]] = [i[0]]
#             clothes_types.append(i[1])
#         else:
#             clothes_hm[i[1]].append(i[0])
    
#     result = 0
#     for i in range(1, len(clothes_hm)+1):
#         combi = list(combinations(clothes_types, i))
#         for j in combi:
#             if len(j) == 1: # 한 종류의 옷으로만 입는 경우, ('eyewear',)
#                 result += len(clothes_hm[j[0]])
#             else: # 최소 두 종류의 옷을 섞어 입는 경우
#                 temp = 1
#                 for k in j: # ('headgear', 'eyewear')
#                     temp *= len(clothes_hm[k])
#                 result += temp
#     return result

def solution(clothes):
    clothes_hm = {}
    # Count the number of each type of clothes
    for cloth, cloth_type in clothes:
        clothes_hm[cloth_type] = clothes_hm.get(cloth_type, 0) + 1

    # Calculate the total combinations considering each type of clothes
    # If there are n types of clothes, the number of combinations would be (a+1)*(b+1)*...(n+1) - 1
    total_combinations = 1
    for count in clothes_hm.values():
        total_combinations *= (count + 1)

    # Subtract 1 to exclude the case of wearing no clothes at all
    return total_combinations - 1