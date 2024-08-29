# 이름 - 점수 별 해시테이블
# photo 를 반복하면서 각 사진에 나오는 인물로 name 으로 해시테이블 점수 계산
# 한번 사진 끝날 때 마다 answer 에 합산 점수 반영
def solution(name, yearning, photo):
    answer = []
    score_table = {}
    for i in range(len(name)):
        score_table[name[i]] = yearning[i]
        
    for picture in photo:
        score = 0
        for name in picture:
            if name in score_table:
                score += score_table[name]
        answer.append(score)
    return answer