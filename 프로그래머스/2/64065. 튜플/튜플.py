# def solution(s):
#     answer = []
#     tup = ()
#     stack = []
#     tmp = []
#     s2 = []
#     max_len = 0
#     for i in s:
#         if i == ',':
#             continue
        
#         if i == '{':
#             stack.append('{')
#         elif i == '}' and stack[-1] == '{':
#             stack.pop()
#             s2.append(tmp)
#             tmp = []
#         else:
#             tmp.append(int(i))
        
#     print(s2)
#     print(s.split('},{'))
#     l = s.split('},{')
#     l[0] = l[0].replace('{{', '')
#     l[-1] = l[-1].replace('}}', '')
#     print(l)
#     tt = set()
#     for i in l:
#         t = i.split(',')
#         if len(t) == 1:
#             tt.add(int(i))
#         else:
#             for j in t:
#                 tt.add(int(j))
#     print(list(tt))
#     return list(tt)

def solution(s):
    answer = []
    result = []
    parts = s.strip('{}').split('},{')
    for part in parts:
        numbers = [int(num) for num in part.split(',')]
        result.append(numbers)
    
    s2 = sorted(result, key=len)
    answer.append(s2[0][0])
    for i in range(len(s2)):
        if i+1 > len(s2)-1:
            break
        answer.append(list(set(s2[i+1]) - set(s2[i]))[0])
    return answer

