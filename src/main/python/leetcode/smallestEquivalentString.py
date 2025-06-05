class UnionFind:
    def __init__(self):
        self.parent = {chr(x) : chr(x) for x in range(ord('a'), ord('z') + 1)}
        self.size = {chr(x) : 1 for x in range(ord('a'), ord('z') + 1)}
        self.min_element = {chr(x) : chr(x) for x in range(ord('a'), ord('z') + 1)}

    def find_parent(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find_parent(self.parent[a])
        return self.parent[a]
    
    def union_sets(self, a, b):
        u, v = self.find_parent(a), self.find_parent(b)
        if u == v: return
        if self.size[u] < self.size[v]:
            u, v = v, u
        self.min_element[u] = min(self.min_element[u], self.min_element[v])
        self.parent[v] = u
        self.size[u] += self.size[v]

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind()
        for a, b in zip(s1, s2):
            uf.union_sets(a, b)
        
        return ''.join([uf.min_element[uf.find_parent(c)] for c in baseStr])
