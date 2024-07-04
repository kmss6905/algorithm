def solution(m, n, puddles):
    
    _map = [[0 for j in range(m+1)] for i in range(n+1)]
    _map[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] in puddles:
                continue
            if i == 1 and j == 1:
                continue
            _map[i][j] = _map[i][j-1] + _map[i-1][j]
    return _map[n][m] % (1000000007)