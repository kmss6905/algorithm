import sys
a = int(sys.stdin.readline())
answer = []
for _ in range(a):
    b, c = map(int, sys.stdin.readline().split())
    answer.append(b+c)

for i in answer:
    print(i)