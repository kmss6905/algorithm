a = int(input())
b = []
for _ in range(a):
    n, m = map(int, input().split())
    b.append(n + m)

for _ in b:
    print(_)
