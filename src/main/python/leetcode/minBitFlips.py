class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        # XOR the start and goal to find the differing bits
        xor_result = start ^ goal
        
        # Count the number of 1's in the binary representation of xor_result
        return bin(xor_result).count('1')
