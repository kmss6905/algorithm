# Union-Find (Disjoint Set Union) 자료구조 구현
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# 입력 받기
x, y = map(int, input().split())
edges = []
for _ in range(y):
    a, b, c = map(int, input().split())
    edges.append((c, a-1, b-1))  # 1-based index를 0-based index로 변환

# Kruskal 알고리즘을 사용하여 최소 스패닝 트리 찾기
edges.sort()  # 간선들을 가중치 순으로 정렬
uf = UnionFind(x)
result = 0
for cost, a, b in edges:
    if uf.find(a) != uf.find(b):
        uf.union(a, b)
        result += cost

print(result)
