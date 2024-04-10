d = {}
for i in range(1, 31):
    d[i] = False

for _ in range(28):
    a = int(input())
    if a in d:
        d[a] = True

answer = []

for i in d:
    if d[i] == False:
        answer.append(i)

for i in sorted(answer):
    print(i)
    