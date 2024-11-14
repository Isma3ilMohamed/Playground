from typing import List
import math

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        # Define the binary search bounds
        left, right = 1, max(quantities)
        
        # Helper function to determine if a given max load per store is feasible
        def canDistribute(mid: int) -> bool:
            required_stores = 0
            for quantity in quantities:
                required_stores += math.ceil(quantity / mid)
                if required_stores > n:
                    return False
            return required_stores <= n
        
        # Binary search to find the minimized maximum
        while left < right:
            mid = (left + right) // 2
            if canDistribute(mid):
                right = mid  # Try for a smaller maximum
            else:
                left = mid + 1  # Increase the maximum
                
        return left
