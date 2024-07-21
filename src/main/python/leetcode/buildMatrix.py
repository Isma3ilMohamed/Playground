class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topological_sort(n: int, conditions: List[List[int]]) -> List[int]:
            # Build the graph
            graph = defaultdict(list)
            indegree = [0] * (n + 1)
            for u, v in conditions:
                graph[u].append(v)
                indegree[v] += 1
            
            # Perform topological sort
            queue = deque([i for i in range(1, n + 1) if indegree[i] == 0])
            topo_order = []
            while queue:
                node = queue.popleft()
                topo_order.append(node)
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            if len(topo_order) == n:
                return topo_order
            else:
                return []

        row_order = topological_sort(k, rowConditions)
        col_order = topological_sort(k, colConditions)
        
        if not row_order or not col_order:
            return []
        
        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}
        
        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num
        
        return matrix
