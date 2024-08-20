def solution(my_string, m, c):
    answer = ''
    for idx, e in enumerate(list(my_string)):
        if idx % m == c-1:
            answer += my_string[idx]
    return answer