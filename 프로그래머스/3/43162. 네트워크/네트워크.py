"""
컴퓨터 개수 1 이상 200 이하
전형적인 섬의 개수 찾기
1. 그래프 구현 -> 조금 해메는 ?
2. BFS
3. count 네트워크 개수

"""
from collections import deque

def solution(n, computers):
  visited = [False] * n
  graph = {}
  for i in range(n):
    graph[i] = []

  # 그래프 구현
  for i in range(len(computers)):
    for j in range(len(computers[0])):
      if computers[i][j] == 1:
        graph[i].append(j)

  def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
      node = q.popleft()

      for next_node in graph[node]:
        if not visited[next_node]:
          q.append(next_node)
          visited[next_node] = True

  answer = 0
  for key in graph.keys():
    if not visited[key]:
      bfs(key)
      answer += 1

  return answer