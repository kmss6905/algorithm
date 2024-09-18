def solutions():
    cnt = 0
    n, k = map(int, input().split())
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
            if cnt == k:
                return i
    
    if cnt < k:
        return 0
        
if __name__ == '__main__':
    print(solutions())