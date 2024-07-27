
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # Initialize the distance matrix with infinity
        inf = float('inf')
        dist = [[inf] * 26 for _ in range(26)]
        
        # Distance to itself is 0
        for i in range(26):
            dist[i][i] = 0
        
        # Fill in the initial costs from the given transformations
        for o, c, w in zip(original, changed, cost):
            u = ord(o) - ord('a')
            v = ord(c) - ord('a')
            dist[u][v] = min(dist[u][v], w)
        
        # Floyd-Warshall algorithm to find the shortest path between all pairs of nodes
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dist[i][k] < inf and dist[k][j] < inf:
                        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        # Calculate the total cost to convert source to target
        total_cost = 0
        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == inf:
                return -1
            total_cost += dist[u][v]
        
        return total_cost
