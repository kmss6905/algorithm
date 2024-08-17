def solution(myString):
    answer = []
    l = myString.split('x')
    for i in l:
        answer.append(len(i))
    return answer