def sol():
    n = int(input())
    answer = []

    # 1000 * 10 * log10 = 10000 * 3.xxx
    for _ in range(n):
        l = list(map(int, input().split()))
        l.sort()
        answer.append(l[-3])

    for i in answer:
        print(i)


if __name__ == '__main__':
    sol()
