import sys

a = int(sys.stdin.readline())
nums = [0] + list(map(int, sys.stdin.readline().split()))
prefix_sums = [0] * (len(nums) + 1)

for i in range(1, len(nums)):
    prefix_sums[i] = prefix_sums[i-1] + nums[i];

b = int(input())
answer = []
for _ in range(b):
    x, y = map(int, sys.stdin.readline().split())
    answer.append(prefix_sums[y] - prefix_sums[x-1])

for i in answer:
    print(i)
