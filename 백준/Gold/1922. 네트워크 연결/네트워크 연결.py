n = int(input())
paths = []
for _ in range(int(input())):
    a, b, c = map(int, input().split())
    paths.append((a, b, c))

result = 0
paths.sort(key=lambda x:x[2])
connect = set([int(paths[0][0])])
while len(connect) != n:
    for edge in paths:
        a, b, cost = edge
        if a in connect and b in connect:
            continue
        if a in connect or b in connect:
            connect.add(a)
            connect.add(b)
            result += int(cost)
            break
print(result)