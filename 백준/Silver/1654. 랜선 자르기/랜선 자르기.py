def solutions():
    K, target = map(int, input().split())
    lines = []
    for _ in range(K):
        lines.append(int(input()))
    start, end = 1, max(lines)  # 최소 1부터 최대 라인의 길이까지

    def cut(length):
        total = 0
        for line in lines:
            total += line // length
        return total

    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if cut(mid) >= target:  # 잘라낸 개수가 target보다 크거나 같다면
            answer = mid  # 일단 현재 mid 값은 가능한 답
            start = mid + 1  # 더 큰 길이를 시도해 본다
        else:  # 잘라낸 개수가 target보다 작다면
            end = mid - 1  # 길이를 줄여본다

    return answer

if __name__ == '__main__':
    print(solutions())
