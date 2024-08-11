class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        def count_islands(grid):
            def dfs(x, y):
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] == 0:
                    return
                grid[x][y] = 0
                dfs(x + 1, y)
                dfs(x - 1, y)
                dfs(x, y + 1)
                dfs(x, y - 1)
                
            count = 0
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        count += 1
                        dfs(i, j)
            return count
        
        def is_disconnected(grid):
            return count_islands([row[:] for row in grid]) != 1

        # Initial check if the grid is already disconnected
        if is_disconnected(grid):
            return 0

        # Check if removing one cell disconnects the island
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if is_disconnected(grid):
                        return 1
                    grid[i][j] = 1

        # If the island cannot be disconnected by removing one cell, return 2
        return 2
