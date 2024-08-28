def solution(nums):
    sel = len(nums) // 2
    return min(len(set(nums)), sel)