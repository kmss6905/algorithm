# 평행 -> 기울기가 같다(문제에서 겹치는 것 포함)
'''
아이디어

dots 에서 서로 다른 두 점을 선택해서 만들 수 있는 모든 기울 기 구함.
set() 한 결과가 4C2 = 6 이 나오면 1, 그렇지 않으면 0
'''
def solution(dots):
    [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]=dots
    answer1 = ((y1-y2)*(x3-x4) == (y3-y4)*(x1-x2))
    answer2 = ((y1-y3)*(x2-x4) == (y2-y4)*(x1-x3))
    answer3 = ((y1-y4)*(x2-x3) == (y2-y3)*(x1-x4))
    return 1 if answer1 or answer2 or answer3 else 0