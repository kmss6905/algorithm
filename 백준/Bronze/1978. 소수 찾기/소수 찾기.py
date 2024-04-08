a = input()
b = list(map(int, input().split()))
cnt = 0 # 소수가 아닌 것들
for i in b:
    tmp = i
    if tmp == 1:
        cnt += 1
        continue
    while tmp != 2:
        tmp -= 1
        if i % tmp == 0:
            cnt += 1
            break
print(len(b)-cnt)