class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * n for _ in range(m)]
        min_heap = [(grid[0][0], 0, 0)]
        visited[0][0] = True
        points = 0
        
        # Sort queries and keep track of original indices
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        result = [0] * len(queries)
        
        for query, original_index in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                _, x, y = heapq.heappop(min_heap)
                points += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        heapq.heappush(min_heap, (grid[nx][ny], nx, ny))
            result[original_index] = points
        
        return result
