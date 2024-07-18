"""
(2 * 10^6)(2 * 10^8) => 4 * 10 ^ 14

건널 수 있느냐, 없느냐가 핵심 -> 카운트


"""
# def solution(stones, k):
#     answer = 0
#     flag = True
#     step = 0
#     cnt = 0
    # while(flag):
    #     for i in range(len(stones)):
    #         if stones[i] == 0:
    #             step += 1
    #             if step == k:
    #                 flag = False # 건너기 중단
    #                 break
    #             continue
    #         stones[i] -= 1
    #         step = 0
    #     if flag == False:
    #         break
    #     cnt += 1
    # return cnt

"""
200,000,000
100,000,000 -> 10^8

"""
def solution(stones, k):
    
    # 0 이 연달아서 k 만큼 있는 경우아 아니면 된다.
    
    
    
    # 0 2 3 1 0 0 2 0 3 0 => 2 이 뺴기 + 1
    # 0 1 2 0 0 0 1 0 2 0 => x
    # 0 1000000 0 0 1000000, K = 1
    
    
    # 0 0 0 0 0 0 0 0 0 0
    
    # [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

    # 아이디어는 맞았다. 2씩 줄여가면서 하는 것 ! 근데 .. 구현을 못했다.. 구현력 부족
    left = 1
    right = max(stones) + 1
    while left < right - 1:
        mid = (left + right) // 2
        nowk = 0
        flag = True
        for stone in stones:
            if stone < mid:
                nowk+=1
            else:
                nowk = 0
            if nowk == k:
                flag = False
                break
        if flag:
            left = mid
        else:
            right = mid
    return left
    