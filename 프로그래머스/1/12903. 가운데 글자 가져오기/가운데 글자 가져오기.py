def solution(s):
    answer = ''
    if len(s) % 2 == 1:
        return s[(len(s) - 1) // 2]
    else:
        return s[((len(s)) // 2) - 1] + s[(len(s)) // 2]