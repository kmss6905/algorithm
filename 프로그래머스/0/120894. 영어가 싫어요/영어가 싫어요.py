def solution(numbers):
    answer = ''
    for i in range(len(numbers)):
        if numbers[i:].startswith('zero'):
            answer += '0'
        
        if numbers[i:].startswith('one'):
            answer += '1'
        
        if numbers[i:].startswith('two'):
            answer += '2'
            
        if numbers[i:].startswith('three'):
            answer += '3'
        
        if numbers[i:].startswith('four'):
            answer += '4'
        
        if numbers[i:].startswith('five'):
            answer += '5'
        
        if numbers[i:].startswith('six'):
            answer += '6'
        
        if numbers[i:].startswith('seven'):
            answer += '7'
            
        if numbers[i:].startswith('eight'):
            answer += '8'
            
        if numbers[i:].startswith('nine'):
            answer += '9'
    return int(answer)