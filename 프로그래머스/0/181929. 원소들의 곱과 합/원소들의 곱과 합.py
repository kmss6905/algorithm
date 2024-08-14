def solution(num_list):
    multi = 1
    sumi = 0
    for i in num_list:
        multi *= i
        sumi += i
    
    return 1 if multi < sumi * sumi else 0 