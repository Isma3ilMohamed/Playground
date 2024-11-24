from typing import List

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_abs = float('inf')
        negative_count = 0
        
        # Traverse the matrix
        for row in matrix:
            for num in row:
                total_sum += abs(num)  # Add absolute value to the total sum
                min_abs = min(min_abs, abs(num))  # Track the smallest absolute value
                if num < 0:
                    negative_count += 1  # Count negatives
        
        # Adjust the total sum if the number of negatives is odd
        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs
        
        return total_sum
