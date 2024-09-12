def sol(num):
    a = input().rstrip().split(' ')
    _map = {}
    for v in a:
        _map[v] = True

    b = int(input())
    c = input().rstrip().split(' ')
    d = []
    for v in c:
        if v in _map:
            print(1)
        else:
            print(0)
            
            
sol(int(input()))