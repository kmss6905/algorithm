m = 0
mi = 0
for i in range(9):
    a = int(input())
    if a > m:
        m = a
        mi = i

print(m)
print(mi+1)