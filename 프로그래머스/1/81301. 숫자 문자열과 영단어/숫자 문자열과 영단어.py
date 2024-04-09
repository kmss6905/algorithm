num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}

def solution(s):
    answer = ''
    temp = ''
    for char in s:
        if char.isalpha():
            temp += char
            if temp in num_dic:
                answer += num_dic[temp]
                temp = ''
        else:
            answer += char
    return int(answer)