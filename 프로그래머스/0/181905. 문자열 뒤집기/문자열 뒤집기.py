# 파이썬 문자열 뒤집기
"""
1. for
a = "hello world"
c = ''
result = ''
for i in a:
    result = i + c # 앞에다 계속 더하는 방법
    

2. list -> reverse -> join -> str 
''.join(list(a).reverse())

3. str[::-1]

"""

def solution(my_string, s, e):
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]