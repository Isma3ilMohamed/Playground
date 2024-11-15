from typing import List

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Step 1: Find the longest non-decreasing prefix
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        
        # If the entire array is already sorted, no need to remove anything
        if left == n - 1:
            return 0
        
        # Step 2: Find the longest non-decreasing suffix
        right = n - 1
        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1
        
        # Minimum length of subarray to remove (initially assume removing middle section entirely)
        min_remove = min(n - left - 1, right)
        
        # Step 3: Try to merge prefix and suffix
        i, j = 0, right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                min_remove = min(min_remove, j - i - 1)
                i += 1
            else:
                j += 1
        
        return min_remove
