a = input().upper()
d = {}
for i in a:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
# 일반적인 패턴은 객체의 인덱스 중 일부를 키로 사용하여 복잡한 객체를 정렬하는 것입니다. 
sd = sorted(d, key=lambda x:d[x], reverse=True)
if len(sd) == 1:
    print(sd[0])
elif d[sd[0]] == d[sd[1]]:
    print('?')
else:
    print(sd[0])