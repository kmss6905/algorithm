a = input()
al = len(a)
for i in range(len(a)):
    b = a[i::]
    c = b[::-1]
    if b == c:
        print(al+i)
        break