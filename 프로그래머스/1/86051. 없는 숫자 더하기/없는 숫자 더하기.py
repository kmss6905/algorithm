def solution(numbers):
    l = set(list(range(10))) - set(numbers)
    return sum(l)