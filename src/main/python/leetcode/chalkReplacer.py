from typing import List

class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        # Calculate the total chalk usage in one full cycle
        total_chalk = sum(chalk)
        
        # Reduce k by the total chalk used in full cycles
        k %= total_chalk
        
        # Find the student who will run out of chalk
        for i, c in enumerate(chalk):
            if k < c:
                return i
            k -= c
