from typing import List

class Solution:
    def dfs(self, adjList: List[List[int]], visited: List[bool], src: int) -> None:
        visited[src] = True
        for neighbor in adjList[src]:
            if not visited[neighbor]:
                self.dfs(adjList, visited, neighbor)

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        # Initialize the number of connected components and visited list.
        components = 0
        visited = [False] * n
        adjList = [[] for _ in range(n)]
        
        # Build the adjacency list.
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        
        # Perform DFS for each unvisited node.
        for i in range(n):
            if not visited[i]:
                components += 1
                self.dfs(adjList, visited, i)
                
        return components
