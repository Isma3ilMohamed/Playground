class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i: int, m: int) -> int:
            if i == len(piles):
                return 0
            
            max_stones = 0
            current_sum = 0
            
            for x in range(1, 2 * m + 1):
                if i + x > len(piles):
                    break
                
                current_sum += piles[i + x - 1]
                max_stones = max(max_stones, current_sum + sum(piles[i + x:]) - dp(i + x, max(m, x)))
            
            return max_stones
        
        total_sum = sum(piles)
        return dp(0, 1)
