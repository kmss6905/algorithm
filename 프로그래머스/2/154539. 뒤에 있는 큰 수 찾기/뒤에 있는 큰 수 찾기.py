"""
n^2 불가

완전탐색 x
def solution(numbers):
    answer = []
    for idx, e in enumerate(numbers):
        a = -1
        for j in range(idx+1, len(numbers)):
            if e >= numbers[j]:
                continue
            a = numbers[j]
            
            break
        answer.append(a)
    return answer

미리저장해놓기 ? -> stack 을 활용

"""
"""def solution(numbers):
    # number index 정보를 담을 Stack 생성
    stack = []

    # 정답 배열 생성
    answer = [0] * len(numbers)

    # 첫 번째 number 인덱스 stack에 push
    stack.append(0)

    # 두 번째 원소부터 numbers 탐색
    for i in range(1, len(numbers)):
        # 스택이 비어있지 않으면서 현재 스택이 바라보고 있는 값보다 number의 값이 크면 뒤에 있는 큰 수 해당
        while stack and numbers[stack[-1]] < numbers[i]:
            # 뒤에 있는 큰 수에 해당하는 모든 값 pop
            answer[stack.pop()] = numbers[i]
        # 현재 인덱스 push
        stack.append(i)

    # 현재 스택이 바라보고 있는 값보다 number 의 값이 큰 경우가 없는 경우에는 -1
    while stack:
        answer[stack.pop()] = -1

    return answer
"""

"""
stack 은 자기 자신보다 큰 수가 나올 때 까지 임시로 저장해두는 공간
큰 수가 나오면 pop

"""
def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    stack.append(0)
    for i in range(1, len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    while stack:
        answer[stack.pop()] = -1
    
    return answer