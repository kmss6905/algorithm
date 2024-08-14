def solution(my_string, is_prefix):
    lms = len(my_string)
    lpre = len(is_prefix)
    for i in range(lpre):
        if lms < lpre:
            return 0
        else:
            if is_prefix[i] != my_string[i]:
                return 0
    return 1