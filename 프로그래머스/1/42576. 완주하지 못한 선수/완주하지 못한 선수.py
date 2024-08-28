from collections import defaultdict

def solution(participant, completion):
    answer = ''
    parti_dic = defaultdict(int)
    for name in participant:
        parti_dic[name] += 1
    
    for name in completion:
        parti_dic[name] -= 1

    for key, value in parti_dic.items():
        if value != 0:
            answer = key
            break
            
    return answer