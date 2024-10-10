from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        max_width = 0

        # Step 1: Build a decreasing stack of indices
        for i in range(n):
            if not stack or nums[i] < nums[stack[-1]]:
                stack.append(i)
        
        # Step 2: Traverse from the end to start
        for j in range(n - 1, -1, -1):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j - i)
        
        return max_width