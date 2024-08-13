def solution(lines):
    answer = 0
    result = [0] * 200
    
    for line in lines:
        start = line[0]
        end = line[1]
        
        for dot in range(start, end):
            result[dot+100] += 1
    
    for i in result:
        if i >= 2:
            answer += 1
    return answer