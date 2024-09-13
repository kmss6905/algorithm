def solutions():
    K, target = map(int, input().split())
    lines = []
    # O (N)
    for _ in range(K):
        lines.append(int(input()))
    start, end = 1, max(lines)

    # 자를 때 마다 O(N) , N(K) = 10,000
    def cut(length):
        total = 0
        for line in lines:
            total += line // length
        return total

    # O(k log N)
    # 문제에서는 최대의 길이를 물어봤기 때문에
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if cut(mid) >= target:  # 좀 더 크게 잘라본다.
            answer = mid
            start = mid + 1
        else:  # 잘라낸 개수가 target보다 작다면
            end = mid - 1
    return answer


if __name__ == '__main__':
    print(solutions())


