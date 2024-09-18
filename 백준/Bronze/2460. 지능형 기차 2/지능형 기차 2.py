total = 0
mt = 0
for _ in range(10):
    left, on =  map(int, input().split())
    total += on
    total -= left
    mt = max(mt, total)
print(mt)
