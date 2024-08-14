def solution(num_list):
    oddsum = ''
    evensum = ''
    
    for i in num_list:
        if i % 2 == 0:
            evensum += str(i)
        else:
            oddsum += str(i)
    
    return int(oddsum) + int(evensum)