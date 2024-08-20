"""
joystick=dict(zip([1,-1,10,-10],['w','s','d','a']))
    for i in range(1,len(log)):
        res+=joystick[log[i]-log[i-1]]
"""
def solution(numLog):
    op = {'1': 'w', '-1':'s', '10': 'd', '-10': 'a'}
    answer = ''
    for i in range(1, len(numLog)):
        answer += op[str(numLog[i] - numLog[i-1])]
    return answer