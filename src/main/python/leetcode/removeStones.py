class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

class Solution:
    def removeStones(self, stones) -> int:
        uf = UnionFind()
        
        for x, y in stones:
            uf.add(x)
            uf.add(~y)  # Use ~y to distinguish between rows and columns
            uf.union(x, ~y)

        # Count the number of unique components
        unique_components = len(set(uf.find(x) for x, y in stones))

        # The number of stones that can be removed is total stones - number of components
        return len(stones) - unique_components
