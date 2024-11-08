from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        max_xor_value = (1 << maximumBit) - 1  # This is 2^maximumBit - 1, all bits set to 1 within maximumBit range
        prefixXOR = 0
        result = []
        
        # Calculate cumulative XOR for the prefix
        for num in nums:
            prefixXOR ^= num
            # Append the maximum XOR with the all-bits set value
            result.append(prefixXOR ^ max_xor_value)
        
        # Reverse the result as specified by the problem statement
        return result[::-1]
