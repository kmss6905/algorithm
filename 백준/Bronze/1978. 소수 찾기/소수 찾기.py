def sol():
    n = int(input())
    m = map(int, input().split())
    answer = 0
    for i in m:
        num = 0
        for j in range(1, i+1):
            if i % j == 0:
                num += 1

        if num == 2:
            answer += 1
    return answer

if __name__ == '__main__':
    print(sol())
