a = int(input())
answer = []
for _ in range(a):
    b = input()
    answer.append(b[0]+b[-1])
for i in answer:
    print(i)