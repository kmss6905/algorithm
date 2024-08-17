def solution(my_string, num1, num2):
    answer = ''
    a = list(my_string)
    temp = a[num1]
    a[num1] = a[num2]
    a[num2] = temp
    
    return ''.join(a)