class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Initialize the distances matrix
        inf = float('inf')
        dist = [[inf] * n for _ in range(n)]
        
        # Distance to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Fill in the distances from the edges
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        
        # Floyd-Warshall algorithm to compute shortest paths between all pairs of nodes
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Find the city with the smallest number of neighbors within the distance threshold
        min_count = inf
        result = -1
        
        for i in range(n):
            count = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    count += 1
            # We subtract 1 to not count the city itself
            count -= 1
            
            if count < min_count or (count == min_count and i > result):
                min_count = count
                result = i
        
        return result
