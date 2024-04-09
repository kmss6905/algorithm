a = int(input())
cnt = 0
for _ in range(a):
    s = set()
    b = list(input())
    ng = 0
    for i, v in enumerate(b):
        if v not in s:
            s.add(v)
        else:
            if b[i] != b[i-1]:
                ng = 1
                break
    if ng == 0:
        cnt += 1
print(cnt)