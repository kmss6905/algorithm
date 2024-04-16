a,b = map(int, input().split())
l = [i for i in range(1, a+1)]
for _ in range(b):
    x, y = map(int, input().split())
    tmp = l[y-1]
    l[y-1] = l[x-1]
    l[x-1] = tmp

for i in l:
    print(i, end=" ")