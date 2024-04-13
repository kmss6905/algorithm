import sys

a, b = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

prefix_sums = [0] * (a + 1)
prefix_sums[1] = nums[0]
for i in range(1, a):
    prefix_sums[i + 1] = prefix_sums[i] + nums[i]

count = 0
sum_count = {0: 1}

for i in range(1, a + 1):
    count += sum_count.get(prefix_sums[i] - b, 0)
    sum_count[prefix_sums[i]] = sum_count.get(prefix_sums[i], 0) + 1

print(count)
