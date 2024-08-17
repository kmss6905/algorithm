# 알파벳 순서에서 "l"보다 앞서
def solution(myString):
    answer = ''
    for i in myString:
        if i <= 'l':
            answer += 'l'
            continue
            
        answer += i
            
    return answer