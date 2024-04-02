import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

p = {}
visited = set()  # Use set instead of list for faster membership check
q = deque([1])
visited.add(1)
while q:
    cur_n = q.popleft()
    for i in graph[cur_n]:
        if i not in visited:  # Set membership check is faster
            p[i] = cur_n
            visited.add(i)  # Use add() method to add elements to the set
            q.append(i)

for i in range(2, n+1):
    sys.stdout.write(str(p[i]) + '\n')
