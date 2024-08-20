def solution(binomial):
    answer = 0
    nomals = binomial.split(' ')
    op = nomals[1]
    if op == '+':
        return int(nomals[0]) + int(nomals[2])
    elif op == '-':
        return int(nomals[0]) - int(nomals[2])
    elif op == '*':
        return int(nomals[0]) * int(nomals[2])
    return answer