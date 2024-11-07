from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        # Initialize an array to keep track of counts for each bit position (up to 24 bits for typical integer range)
        bit_count = [0] * 24
        
        # Count the number of 1s in each bit position across all candidates
        for num in candidates:
            for bit in range(24):  # Assume numbers fit within 24 bits
                if num & (1 << bit):  # Check if the bit is set
                    bit_count[bit] += 1
        
        # The answer is the maximum count of 1s in any bit position
        return max(bit_count)
