def solution(num_list):
    num_list = [0] + num_list
    even_sum = 0
    odd_sum = 0
    
    for idx, e in enumerate(num_list):
        if idx % 2 == 0:
            odd_sum += e
        else:
            even_sum += e
    return max(even_sum, odd_sum)