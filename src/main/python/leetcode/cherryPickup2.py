class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        cache = {}

        def dfs(r, col1, col2):
            if (r, col1, col2) in cache:
                return cache[(r, col1, col2)]
            if col1 == col2 or min(col1, col2) < 0 or max(col1, col2) == COLS:
                return 0
            if r == ROWS - 1:
                return grid[r][col1] + grid[r][col2]
            res = 0
            for col1_d in [-1, 0, 1]:
                for col2_d in [-1, 0, 1]:
                    res = max(res, dfs(r + 1, col1 + col1_d, col2 + col2_d))

            cache[(r, col1, col2)] = res + grid[r][col1] + grid[r][col2]
            return cache[(r, col1, col2)]

        return dfs(0, 0, COLS - 1)
