from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, m: int) -> List[int]:
        # Calculate the sum of all rolls (both observed and missing)
        total_sum = (len(rolls) + m) * mean
        sum_observed = sum(rolls)
        
        # Calculate the sum required for the missing rolls
        sum_missing = total_sum - sum_observed
        
        # If the sum_missing is not possible to distribute between m dice, return []
        if sum_missing < m or sum_missing > 6 * m:
            return []
        
        # Start with each missing roll being 1
        result = [1] * m
        sum_missing -= m  # Adjust the sum by subtracting 1 for each dice
        
        # Distribute the remaining sum to maximize the values
        for i in range(m):
            if sum_missing > 0:
                # Distribute the remaining sum, up to 5 (because each dice can be at most 6)
                add = min(5, sum_missing)
                result[i] += add
                sum_missing -= add
        
        return result
