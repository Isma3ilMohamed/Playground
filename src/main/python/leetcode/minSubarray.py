from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_mod = sum(nums) % p
        if total_mod == 0:
            return 0  # The total sum is already divisible by p
        
        prefix_sums = {0: -1}  # Initialize with 0 sum at index -1
        prefix_sum_mod = 0
        min_length = len(nums)
        
        for i, num in enumerate(nums):
            prefix_sum_mod = (prefix_sum_mod + num) % p
            needed = (prefix_sum_mod - total_mod) % p
            if needed in prefix_sums:
                min_length = min(min_length, i - prefix_sums[needed])
            prefix_sums[prefix_sum_mod] = i  # Update the hashmap with the current prefix sum
            
        if min_length == len(nums):
            return -1  # Cannot remove the whole array
        else:
            return min_length
