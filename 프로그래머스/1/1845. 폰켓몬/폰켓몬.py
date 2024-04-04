def solution(nums):
    n = len(nums)/2
    m = len(set(nums))
    return m if n >= m else n