from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Step 1: Calculate LIS for each position
        LIS = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        
        # Step 2: Calculate LDS for each position
        LDS = [1] * n
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]:
                    LDS[i] = max(LDS[i], LDS[j] + 1)
        
        # Step 3: Find the maximum mountain length
        max_mountain_length = 0
        for i in range(1, n - 1):
            if LIS[i] > 1 and LDS[i] > 1:
                max_mountain_length = max(max_mountain_length, LIS[i] + LDS[i] - 1)
        
        # Step 4: Calculate the minimum removals
        return n - max_mountain_length if max_mountain_length > 0 else n
