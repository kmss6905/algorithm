"""
1. 아이디어
해시테이블, key-value 저장

2. 구현
participant -> 딕셔너리 저장 
key 선수이름, value 는 +1

completion 돌면서 해당되는 key 없으면 해당 key return
있는 경우에는 에 -1 씩 함. 

전부 돌고 최종 결과에서 value 가 1이 있인 key(참가자 이름) return

"""
def solution(participant, completion):
    answer = ''
    _map = {}
    for person in participant:
        if person not in _map:
            _map[person] = 1
        else:
            _map[person] += 1
    
    for person in completion:
        if person not in _map:
            answer = person
            return person
        _map[person] -= 1
    
    # check
    for person in _map:
        if _map[person] == 1:
            return person