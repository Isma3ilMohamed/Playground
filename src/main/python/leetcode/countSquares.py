from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        total_squares = 0
        
        for i in range(rows):
            for j in range(cols):
                # Only calculate dp[i][j] if matrix[i][j] is 1
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # Edge case: first row or first column
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    total_squares += dp[i][j]
        
        return total_squares
