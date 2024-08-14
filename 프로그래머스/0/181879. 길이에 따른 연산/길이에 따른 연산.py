def solution(num_list):
    answer = 0
    if len(num_list) >= 11:
        answer = sum(num_list)

    else:
        c = 1
        for i in num_list:
            c *= i
        answer = c
    return answer