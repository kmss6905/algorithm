def solution(genres, plays):
    answer = []
    genres_plays_dic = {}
    geners_plays_sum = {}
    for i in range(len(genres)):
        if genres[i] not in genres_plays_dic:
            genres_plays_dic[genres[i]] = [(i, plays[i])]
            geners_plays_sum[genres[i]] = plays[i]
        else:
            genres_plays_dic[genres[i]].append((i, plays[i]))
            geners_plays_sum[genres[i]] += plays[i]
    
    sorted_data = dict(sorted(geners_plays_sum.items(), key=lambda x: x[1], reverse=True))
    
    for genres in sorted_data: # "classic"
        sorted_genres = sorted(genres_plays_dic[genres], key=lambda x: x[1], reverse=True)
        print(sorted_genres)
        # 장르에 속한 곡이 하나 인 경우
        if len(genres_plays_dic[genres]) == 1:
            answer.append(sorted_genres[0][0])
        else:
            answer.append(sorted_genres[0][0])
            answer.append(sorted_genres[1][0])
    
    return answer