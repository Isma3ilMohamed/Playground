class Solution:
    from typing import List
    
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1 or k == n:
            return 0
        
        # Calculate the cost of each possible bag
        costs = [weights[i] + weights[i + 1] for i in range(n - 1)]
        
        # Sort the costs to find the minimum and maximum possible scores
        costs.sort()
        
        # The minimum score is the sum of the smallest k-1 costs
        min_score = sum(costs[:k-1])
        
        # The maximum score is the sum of the largest k-1 costs
        max_score = sum(costs[-(k-1):])
        
        return max_score - min_score
