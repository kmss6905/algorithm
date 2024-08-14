def solution(myString):
    answer = ''
    for i in myString:
        if i == 'a':
            answer += 'A'
            continue
            
        if i.isupper() and i != 'A':
            answer += i.lower()
            continue
        
        answer += i
    return answer