# s -> 반복해서 돈다.
# stack 글자 넣기 -> 넣을 때 넣을려고 하는 캐릭터 == 마지막 stack 캐릭터 같으면 stack 마지막 빼기
# 모든 글자 스택에 넣었을 때 스택이 비어있으면 1 아니면 0
def solution(s):
    stack = []
    for i in s:
        if len(stack) != 0 and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)
    return 1 if len(stack) == 0 else 0