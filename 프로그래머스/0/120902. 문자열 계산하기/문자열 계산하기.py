def solution(my_string):
    answer = 0
    # 1. string -> split. list 에 담고
    # 2. 첫 결과 0 에서 리스트 반복문 돌면서 + , - 인 경우는 해당 연산 적용 + 인지 - 인지 저장함
    # 3. 최종 결과는 answer 에 담음
    ops = my_string.split(' ')
    plusop = True
    for i in ops:
        if i == '+':
            plusop = True
            continue
        if i == '-':
            plusop = False
            continue
            
        # 처음 0 에서 어떤 것을 더하면 그게 곧 answer 초기화와 같다.
        if plusop:
            answer += int(i)
        else:
            answer -= int(i)
    
    return answer