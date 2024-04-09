l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
for i in l:
    a = a.replace(i, '*')
print(len(a))