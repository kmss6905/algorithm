
def solution(participant, completion):
    pm = {}
    cm = {}
    for i in participant:
        if i not in pm:
            pm[i] = 1
        else:
            pm[i] += 1
    
    for i in completion:
        if i not in cm:
            cm[i] = 1
        else:
            cm[i] += 1
    
    for i in pm:
        if i not in cm or cm[i] != pm[i]:
            return i