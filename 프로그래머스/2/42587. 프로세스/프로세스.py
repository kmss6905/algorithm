from collections import deque

# 처음했던 풀이
def solution(priorities, location):
    answer = 0
    dic = {}
    process_number = []
    for i, v in enumerate(priorities):
        dic[i] = v
        
    # 실행하려고 하는 프로세스가 원래 location 에 위치하던 것이냐?
    
    while len(priorities) != 0:
        a = priorities.pop(0) # O(n)이 priorities 길이가 0이 될 때까지 진행
        if len(priorities) == 0:
            return answer
        if a < max(priorities):
            priorities.append(a) # O(1)
        else:
            answer += 1
            process_number.append((answer, a))
            # 만약 location 에 위치했던 프로세스가 실행되는 차례이면?
            if dic[a] == location:
                return answer
    return answer

# def solution(priorities, location):
#     answer = 0
#     dic = {}
#     process_number = []
#     queue = deque(priorities)
    
#     for index, value in enumerate(priorities):
#         dic[index] = value
    
#     while queue:
#         process = queue.popleft()
#         for i in queue:
#             if process < i:
#                 queue.append(process)
#             else:
#                 answer += 1
#                 process_number.append((answer, process))
#                 if dic[location] == process:
#                     return answer
                
#     return answer

def solution(priorities, location):
    answer = 0
    queue = [(i, v) for i, v in enumerate(priorities)]    
    while True:
        process = queue.pop(0)
        if any(process[1] < q[1] for q in queue):
            queue.append(process)
        else:
            answer += 1
            if process[0] == location:
                return answer
    return answer

'''
큐 에서 pop한 프로세스와 그 외 나머지 프로세스 들과 비교하는 과정을 거쳐야 한다.

if pop한 프로세스 < max(priorities): 
    pop한 프로세스 다시 뒤로 보내기 (append)
else:
    프로세스 실행하기
'''