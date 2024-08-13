# 1/2 + 3/4 = 5/4
def solution(numer1, denom1, numer2, denom2):
    answer = []
    bunmo = denom1 * denom2
    bunza = numer1 * denom2 + numer2 * denom1

    bunza_com = []
    bunmo_com = []
    for i in range(1, bunza+1):
        if bunza % i == 0:
            bunza_com.append(i)
    
    for i in range(1, bunmo+1):
        if bunmo % i == 0:
            bunmo_com.append(i)
    
    max_com = max(list(set(bunza_com) & set(bunmo_com)))
    if max_com == 1:
        return [bunza, bunmo]
    return [bunza//max_com, bunmo//max_com]