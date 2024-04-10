def solution(s):
    ls = s.split(" ")
    answer = []
    for word in ls:
        wl = list(word)
        temp = ""
        for i, w in enumerate(wl):
            if i == 0:
                temp += w.upper()
            else:
                temp += w.lower()
        answer.append(temp)
    return ' '.join(answer)