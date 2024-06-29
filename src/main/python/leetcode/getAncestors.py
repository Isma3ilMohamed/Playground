class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Initialize the graph
        graph = defaultdict(list)
        indegree = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        # Kahn's Algorithm for Topological Sorting
        topo_order = []
        queue = deque([i for i in range(n) if indegree[i] == 0])
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Ancestor tracking
        ancestors = [set() for _ in range(n)]
        
        # Process nodes in topological order
        for node in topo_order:
            for neighbor in graph[node]:
                # Add current node to the ancestors of its neighbor
                ancestors[neighbor].add(node)
                # Add ancestors of the current node to the ancestors of its neighbor
                ancestors[neighbor].update(ancestors[node])
        
        # Convert sets to sorted lists
        result = [sorted(list(ancestors[i])) for i in range(n)]
        
        return result
