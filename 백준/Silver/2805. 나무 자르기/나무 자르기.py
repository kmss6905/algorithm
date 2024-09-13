def solutions():
    N, total = map(int, input().split())
    trees = []
    for tree in map(int, input().split()):
        trees.append(tree)
    start, end = 1, max(trees)

    def total_length(length):
        total = 0
        for tree in trees:
            if tree > length:
                total += tree - length
        return total

    answer = 0
    # O(NlogM)
    while start <= end:
        mid = (start + end) // 2  # 절단기 높이
        if total_length(mid) >= total:  # 나무의 길이가 target 보다 같거나 큰 경우 -> 일단 후보군에 들어가되 좀 더 절단기의 크기를 키워보자 
            answer = mid
            start = mid + 1
        else:  # 나무의 길이가 target 보다 작은 경우, 좀 더 절단기 길이를 짧게 하기 
            end = mid - 1
    return answer


if __name__ == '__main__':
    print(solutions())