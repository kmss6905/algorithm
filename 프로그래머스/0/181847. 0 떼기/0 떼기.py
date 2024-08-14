def solution(n_str):
    answer = ''
    ls = list(n_str)
    if ls[0] != '0':
        return n_str
    
    while ls[0] == '0':
        ls = ls[1:]
    
    answer = ''.join(ls)
    return answer