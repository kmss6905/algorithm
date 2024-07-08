"""
genremap = {}
playssum_geners = {}
for len(geners) -> if genere[i] not in geners: -> gemerma[genere[i]] = [plays[i]], if playessum_gueners not in genere[i]
playsum.geners[generp[i]] = plays[i]
el: playsum.geners[generp[i]] += plays[i]
                -> else: -> gemerma[genere[i]].append((i, plays[i]))
                
palysum_geners.sort 정렬 이후 
palysum_geners.sort[0]
palysum_geners.sort[1]

palysum_geners.sort[0] -> genremap -> 찾기 -> 정렬 -> [0][1] 구하기

"""


# def solution(genres, plays):
#     answer = []
#     gm = {}
#     gm_sum = {}
#     for i in range(len(genres)):
#         if genres[i] not in gm:
#             gm_sum[genres[i]] = plays[i]
#             gm[genres[i]] = [(i, plays[i])]
#         else:
#             gm_sum[genres[i]] += plays[i]
#             gm[genres[i]].append((i, plays[i]))
    
#     print(gm)
#     print(gm_sum)
    
#     if len(gm) == 1:
#         for value in gm.values():
#             l = sorted(value, reverse=True, key=lambda x:x[1])
#             if len(l) >= 2:
#                 ll = l[:2]
#                 return [ll[0][0], ll[1][0]]
#             else:
#                 return [l[0][0]]
            
#     sorted_gen = sorted(gm_sum, reverse=True)
#     l = sorted(gm[sorted_gen[0]], reverse=True, key=lambda x:x[1])
#     r = sorted(gm[sorted_gen[1]], reverse=True, key=lambda x:x[1])
    
#     if len(l) == 1:
#         answer.append(l[0][0])
#     else:
#         answer.append(l[0][0])
#         answer.append(l[1][0])
        
#     if len(r) == 1:
#         answer.append(r[0][0])
#     else:
#         answer.append(r[0][0])
#         answer.append(r[1][0])
    
#     return answer






def solution(genres, plays):
    answer = []
    gm = {}
    gm_sum = {}
    
    # Fill the dictionaries with genre information and play counts
    for i in range(len(genres)):
        if genres[i] not in gm:
            gm[genres[i]] = [(i, plays[i])]
            gm_sum[genres[i]] = plays[i]
        else:
            gm[genres[i]].append((i, plays[i]))
            gm_sum[genres[i]] += plays[i]
    
    # Sort genres by total plays in descending order
    sorted_gen = sorted(gm_sum.keys(), key=lambda x: gm_sum[x], reverse=True)
    
    # For each genre, sort the songs by plays in descending order and add the top two to the answer
    for genre in sorted_gen:
        songs = sorted(gm[genre], key=lambda x: x[1], reverse=True)
        answer.extend([song[0] for song in songs[:2]])
    
    return answer







