from typing import List
import bisect

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # Sort the array to facilitate binary search
        nums.sort()
        count = 0
        
        # Iterate through each element, using it as the first element of the pair
        for i in range(len(nums) - 1):
            # Calculate the range of values for nums[j] that makes nums[i] + nums[j] within [lower, upper]
            min_val = lower - nums[i]
            max_val = upper - nums[i]
            
            # Use binary search to find the range of valid indices for nums[j]
            left = bisect.bisect_left(nums, min_val, i + 1)
            right = bisect.bisect_right(nums, max_val, i + 1)
            
            # Add the count of valid pairs for this specific nums[i]
            count += right - left
        
        return count
