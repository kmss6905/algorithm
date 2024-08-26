from itertools import combinations

def solution(number):
    answer = 0
    threes = combinations(number, 3)
    for i in threes:
        if sum(i) == 0:
            answer += 1
    return answer