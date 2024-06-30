class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [1] * size
        self.count = size  # Number of connected components

    def find(self, u):
        if u != self.parent[u]:
            self.parent[u] = self.find(self.parent[u])  # Path compression
        return self.parent[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.rank[rootU] > self.rank[rootV]:
                self.parent[rootV] = rootU
            elif self.rank[rootU] < self.rank[rootV]:
                self.parent[rootU] = rootV
            else:
                self.parent[rootV] = rootU
                self.rank[rootU] += 1
            self.count -= 1
            return True
        return False

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        aliceUF = UnionFind(n + 1)
        bobUF = UnionFind(n + 1)
        usedEdges = 0

        # Step 1: Process type 3 edges first
        for t, u, v in edges:
            if t == 3:
                if aliceUF.union(u, v):
                    bobUF.union(u, v)
                    usedEdges += 1

        # Step 2: Process type 1 and type 2 edges
        for t, u, v in edges:
            if t == 1:
                if aliceUF.union(u, v):
                    usedEdges += 1
            elif t == 2:
                if bobUF.union(u, v):
                    usedEdges += 1

        # Check if both graphs are fully traversable
        if aliceUF.count > 2 or bobUF.count > 2:  # Including the 0th node
            return -1

        # Maximum number of edges to remove
        return len(edges) - usedEdges
