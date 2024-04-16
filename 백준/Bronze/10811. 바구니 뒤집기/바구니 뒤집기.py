a, b = map(int, input().split())

baskets = list(range(1, a+1))

for _ in range(b):
    i, j = map(int, input().split())
    baskets[i-1:j] = reversed(baskets[i-1:j])

print(*baskets)