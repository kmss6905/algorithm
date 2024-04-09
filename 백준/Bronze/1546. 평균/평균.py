n = int(input())
a = list(map(int, input().split()))
bunja = sum(a) * 100
bunmo = max(a) * len(a)
print(bunja / bunmo)