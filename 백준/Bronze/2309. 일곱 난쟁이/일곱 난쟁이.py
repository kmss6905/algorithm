if __name__ == '__main__':
    people = []
    sum = 0
    for _ in range(9):
        tall = int(input())
        people.append(tall)
        sum += tall

    people.sort()
    pivot = sum - 100
    left, right = 0, len(people) - 1
    fake = []
    while left < right:
        if people[left] + people[right] == pivot:
            fake.append(people[left])
            fake.append(people[right])
            break
        if people[left] + people[right] < pivot:
            left += 1
        else:
            right -= 1

    for p in people:
        if p == fake[0] or p == fake[1]:
            continue
        print(p)
