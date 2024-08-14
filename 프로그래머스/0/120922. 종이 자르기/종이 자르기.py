def solution(m, n):
    answer = 0
    
    if m == 1 and n == 1:
        return 0

    if m == 1 and n != 1:
        return n-1
    
    if m != 1 and n == 1:
        return m-1
        
    
    return m-1 + (m * (n-1))
    