def sol():
    N = int(input())
    hm = {}
    for i in map(int, input().split()):
        hm[i] = True

    M = int(input())
    for i in map(int, input().split()):
        if i in hm:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    sol()