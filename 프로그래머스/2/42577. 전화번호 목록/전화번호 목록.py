# 완전탐색으로는 불가능 -> 10^6C2 의 결과 10^8 초과
# 정렬? -> 힌트? 
def solution(phone_book): 
    pb = sorted(phone_book)
    for i in range(len(pb)):
        if i < len(pb) - 1 and pb[i+1].startswith(pb[i]):
            return False
    return True