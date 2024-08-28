def solution(phone_book):
    answer = True
    hash_map = {}
    # O(N)
    for phone in phone_book:
        hash_map[phone] = 1

    # O(N)
    for phone in phone_book:
        prefix = ''
        # O(1) 
        for i in phone: # 최대 문자 길이가 20
            prefix += i
            if prefix in hash_map  and prefix != phone:
                return False
    
    # O(N) + O(20N) -> 20 000 000 < 10 ^ 8 => 시간복잡도 통과
    
    return answer
