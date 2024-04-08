answer = []
for _ in range(int(input())):
    s = ""
    a, b = input().split()
    for i in b:
        s += i * int(a)
        
    answer.append(s)

for i in answer:
    print(i)