def solution(my_string, is_suffix):
    answer = 0
    lms = len(my_string)
    lsf = len(is_suffix)
    
    # 뒤에서 부터 suffix 문자열 길이만큼 자른다.
    if lms >= lsf:
        if my_string[-lsf:] == is_suffix:
            return 1
    return answer