def solution(babbling):
    answer = 0
    words = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        w = bab
        for word in words:
            if word in w:
                w = w.replace(word, '*')
        w = w.replace('*', '')
        if w == '':
            answer += 1
        
    return answer