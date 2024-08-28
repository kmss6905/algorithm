import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1 and scoville[-1] < K:
            return -1
        
        if len(scoville) == 2 and scoville[0] + (scoville[1] * 2) < K:
            return -1
        
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            return answer
        
        s2 = heapq.heappop(scoville)
        next_s = s1 + (s2 * 2)
        heapq.heappush(scoville, next_s)
        answer += 1
    
    return answer