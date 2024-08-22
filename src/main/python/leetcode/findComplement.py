class Solution:
    def findComplement(self, num: int) -> int:
        # Calculate the bitmask: this is a number with all bits set to 1
        # that is the same length as the binary representation of `num`
        bitmask = (1 << num.bit_length()) - 1
        
        # XOR num with the bitmask to get the complement
        return num ^ bitmask
