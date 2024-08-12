# brown, yellow
# 2,000,000 * 5000 = 5 000 000 000 = 10^10
def solution(brown, yellow):
    answer = []
    tbc = brown + yellow
    l = []
    for i in range(1, tbc+1):
        if i * i <= tbc and tbc % i == 0:
            l.append(i)
            l.append(tbc // i)
            
    l = sorted(l)
    
    for row in l:
        col = tbc // row
        if row >= col and (row - 2) * (col - 2) == yellow:
            return [row, col]
    