a, b = map(int, input().split(' '))
l = map(int, input().split(' '))
r = []
for i in l:
    if i < b:
      r.append(str(i))
print(' '.join(r))
