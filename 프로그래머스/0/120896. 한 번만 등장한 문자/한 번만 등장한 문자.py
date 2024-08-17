def solution(s):
    answer = ''
    wordcount = {}
    for i in s:
        if i in wordcount:
            wordcount[i] += 1
            continue
        wordcount[i] = 1
    
    for i in wordcount.keys():
        if wordcount[i] == 1:
            answer += i
        
    return ''.join(sorted(answer))