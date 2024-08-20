# 파이썬 slice 함수를 잘 알고있는가? 하는 문제임
# 단순 구현
def solution(n, slicer, num_list):
    answer = []
    if n == 1:
        return num_list[:slicer[1]+1]
    
    if n == 2:
        return num_list[slicer[0]:]
    
    if n == 3:
        return num_list[slicer[0]:slicer[1]+1]
    
    if n == 4:
        return num_list[slicer[0]:slicer[1]+1:slicer[2]]
    return answer