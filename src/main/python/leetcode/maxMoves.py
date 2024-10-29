from typing import List

class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # DP table to keep track of the maximum moves from each cell
        dp = [[0] * cols for _ in range(rows)]
        
        # Traverse columns from right to left, starting from the second last column
        for j in range(cols - 2, -1, -1):
            for i in range(rows):
                # Check the three possible cells in the next column
                max_moves = 0
                if i > 0 and grid[i][j] < grid[i-1][j+1]:  # Up-right cell
                    max_moves = max(max_moves, dp[i-1][j+1] + 1)
                if grid[i][j] < grid[i][j+1]:               # Right cell
                    max_moves = max(max_moves, dp[i][j+1] + 1)
                if i < rows - 1 and grid[i][j] < grid[i+1][j+1]:  # Down-right cell
                    max_moves = max(max_moves, dp[i+1][j+1] + 1)
                
                dp[i][j] = max_moves  # Store the maximum moves at dp[i][j]
        
        # The answer is the maximum value in the first column
        return max(dp[i][0] for i in range(rows))
