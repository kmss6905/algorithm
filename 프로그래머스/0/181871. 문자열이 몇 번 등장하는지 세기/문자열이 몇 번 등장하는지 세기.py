def solution(myString, pat):
    answer = 0
    pl = len(pat)
    for i in range(len(myString)):
        if myString[i] == pat[0] and i + (len(pat)-1) <= len(myString) - 1:
            if myString[i:i+pl] == pat:
                answer += 1
    return answer