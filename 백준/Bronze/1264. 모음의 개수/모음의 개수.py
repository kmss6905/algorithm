l = []
while True:
    words = input()
    if words == '#':
        break
    cnt = 0
    for i in words:
        # O(1)
        if i in ['a', 'e', 'i', 'o', 'u', 'I', 'E', 'A', 'U', 'O']:
            cnt += 1
    l.append(cnt)
    
for i in l:
    print(i)