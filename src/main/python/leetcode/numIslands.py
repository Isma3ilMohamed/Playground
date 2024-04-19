class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        def dfs(i, j):
            # Check if the current cell is out of bounds or water
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'

            # Traverse all four possible directions
            dfs(i + 1, j)  # down
            dfs(i - 1, j)  # up
            dfs(i, j + 1)  # right
            dfs(i, j - 1)  # left

        count = 0
        # Iterate through each cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an unvisited land cell
                    dfs(i, j)  # Perform DFS from this cell
                    count += 1  # After returning from DFS, increment island count

        return count
