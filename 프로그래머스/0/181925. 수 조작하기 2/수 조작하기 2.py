def solution(numLog):
    op = {'1': 'w', '-1':'s', '10': 'd', '-10': 'a'}
    answer = ''
    for i in range(len(numLog)):
        if i+1 < len(numLog):
            answer += op[str(numLog[i+1] - numLog[i])]
                
    return answer