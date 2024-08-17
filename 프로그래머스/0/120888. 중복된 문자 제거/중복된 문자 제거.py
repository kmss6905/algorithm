def solution(my_string):
    answer = ''
    word = {}
    for i in my_string:
        if i in word:
            continue
        word[i] = True
        answer += i
    
    return answer