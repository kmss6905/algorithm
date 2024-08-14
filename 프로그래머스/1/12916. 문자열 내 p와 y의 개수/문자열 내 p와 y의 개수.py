def solution(s):
    p = 0
    y = 0
    for i in s:
        if i  == 'p' or i == 'P':
            p += 1
            continue
        if i == 'y' or i == 'Y':
            y += 1
            continue
            
    if p == 0 and y == 0:
        return True
        
    return True if p == y else False