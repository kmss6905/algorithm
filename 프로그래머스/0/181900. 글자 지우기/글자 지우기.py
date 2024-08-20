def solution(my_string, indices):
    answer = ''
    ls = list(my_string)
    for i in indices:
        ls[i] = ' '
    
    for i in ls:
        if i == " ":
            continue
        answer += i
    
    return answer