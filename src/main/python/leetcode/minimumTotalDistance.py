from typing import List
import sys
from functools import lru_cache

class Solution:
    def minimumTotalDistance(self, robots: List[int], factories: List[List[int]]) -> int:
        # Sort robots and factories by positions
        robots.sort()
        factories.sort()

        # Extract positions and capacities from factories list
        factory_positions = [pos for pos, cap in factories]
        factory_capacities = [cap for pos, cap in factories]
        
        # Memoization to store results of subproblems
        @lru_cache(None)
        def dp(i, j):
            # Base cases
            if i == len(robots):
                return 0  # All robots assigned
            if j == len(factory_positions):
                return sys.maxsize  # No more factories, but robots remain
            
            # Option 1: Skip the current factory
            min_distance = dp(i, j + 1)
            
            # Option 2: Try to assign up to capacity of current factory
            total_distance = 0
            for k in range(factory_capacities[j]):
                if i + k < len(robots):
                    total_distance += abs(robots[i + k] - factory_positions[j])
                    min_distance = min(min_distance, total_distance + dp(i + k + 1, j + 1))
                else:
                    break
            
            return min_distance
        
        return dp(0, 0)
