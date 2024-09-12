if __name__ == '__main__':
    N = int(input())
    hm = {}
    for i in map(int, input().split()):
        if i in hm:
            hm[i] += 1
        else:
            hm[i] = 1
    M = int(input())
    answer = []
    for i in map(int, input().split()):
        if i in hm:
            answer.append(hm[i])
            continue
        answer.append(0)
    for i in answer:
        print(i, end=' ')
