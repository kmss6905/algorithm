a = int(input())

dic = {0:0, 1:1}
def pibo(n):
    if n in dic:
        return dic[n]
    dic[n] = pibo(n-1) + pibo(n-2) 
    return dic[n]
    

print(pibo(a))