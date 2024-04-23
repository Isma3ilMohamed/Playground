class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        # Build the graph and degree count
        neighbors = defaultdict(list)
        degree = defaultdict(int)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
            degree[u] += 1
            degree[v] += 1

        # Initialize leaves
        leaves = deque()
        for i in range(n):
            if degree[i] == 1:
                leaves.append(i)

        # Trim leaves until reaching the center
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in neighbors[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        # The remaining nodes are the minimum height trees roots
        return list(leaves)
