def solution(myString):
    answer = []
    tmpStr = ''
    for idx, e in enumerate(list(myString)):
        if e != 'x':
            tmpStr += e
            if idx == len(myString) - 1:
                answer.append(tmpStr)
                break
            continue

        if tmpStr != '':
            answer.append(tmpStr)    
            tmpStr = ''
    
    answer.sort()
    return answer
