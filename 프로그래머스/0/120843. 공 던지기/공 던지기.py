def solution(numbers, k): 
    if k == 1:
        return 1
    
    point = 0
    for _ in range(k-1):
        point += 2
        if point >= len(numbers):
            point = point % len(numbers)
            
    return numbers[point]