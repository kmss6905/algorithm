if __name__ == '__main__':
    people = sorted([int(input()) for _ in range(9)])
    pivot = sum(people) - 100

    left, right = 0, 8
    fake1, fake2 = 0, 0

    while left < right:
        if people[left] + people[right] == pivot:
            fake1, fake2 = people[left], people[right]
            break
        if people[left] + people[right] < pivot:
            left += 1
        else:
            right -= 1

    for height in people:
        if height not in (fake1, fake2):
            print(height)
