dic = {}
a = int(input())
temp = {}
answer = []
for _ in range(a):
    b = input()
    if len(b) in dic:
        dic[len(b)].append(b)
    else:
        dic[len(b)] = [b]

for i in sorted(dic.items()):
    if len(i[1]) == 1:
        temp[i[1][0]] = True
        answer.append(i[1][0])
    else:
        for j in sorted(i[1]):
            if j not in temp:
                temp[j] = True
                answer.append(j)
        
for i in answer:
    print(i)