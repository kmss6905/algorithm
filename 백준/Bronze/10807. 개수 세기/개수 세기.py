a = input()
l = list(map(int, input().split()))
b = int(input())
cnt = 0
for i in l:
    if b == i:
        cnt += 1
print(cnt)