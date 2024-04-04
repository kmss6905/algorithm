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
    
    """
    geners_plays_sum 딕셔너리의 각 항목을 재생 횟수(x[1])를 기준으로 내림차순으로 정렬합니다.
    여기서 geners_plays_sum.items()는 딕셔너리의 키-값 쌍을 나타내는 (키, 값) 튜플의 리스트를 반환합니다.
    key=lambda x: x[1] 부분은 각 튜플의 두 번째 요소, 즉 값에 대해 정렬을 수행합니다.
    reverse=True는 역순으로 정렬한다는 것을 의미합니다. 즉, 재생 횟수가 큰 순서대로 정렬됩니다.
    """
    sorted_data = dict(sorted(geners_plays_sum.items(), key=lambda x: x[1], reverse=True))
    
    for genres in sorted_data: # "classic"
        sorted_genres = sorted(genres_plays_dic[genres], key=lambda x: x[1], reverse=True)

        # 장르에 속한 곡이 하나 인 경우
        if len(genres_plays_dic[genres]) == 1:
            answer.append(sorted_genres[0][0])
        else:
            answer.append(sorted_genres[0][0])
            answer.append(sorted_genres[1][0])
    
    return answer