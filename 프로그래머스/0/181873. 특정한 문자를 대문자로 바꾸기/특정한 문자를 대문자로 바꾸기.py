def solution(my_string, alp):
    if alp in my_string:
        return my_string.replace(alp, alp.upper())
    return my_string