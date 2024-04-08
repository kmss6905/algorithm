dic = {}
for i in range(97, 123):
    dic[chr(i)] = -1

answer = []
a = input()
for i, v in enumerate(a):
    if dic[v] == -1:
        dic[v] = i
        
for k, v in dic.items():
    print(v, end=' ')