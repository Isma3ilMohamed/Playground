class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i:[] for i in range(n)}
        visited = set()
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node,visited):
            if node == destination:
                return True
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    if dfs(neighbour,visited):
                        return True
            return False
        
        return dfs(source,visited)
