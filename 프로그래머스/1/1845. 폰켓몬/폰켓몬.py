"""
1. 아이디어
SET 함수를 통한 종류만 추출

2. 
33 2 1 55
1235

3

len(set(nums)) if nums/2 < len(set(nums)) else nums/2

"""
def solution(nums):
    return len(set(nums)) if len(nums)/2 >= len(set(nums)) else len(nums)/2