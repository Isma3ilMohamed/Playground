from typing import List
from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], K: int) -> int:
        # Initialize prefix sum array and deque
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
        
        # Initialize deque and the result variable
        deque_indices = deque()
        min_length = float('inf')
        
        # Iterate through prefix_sum
        for i in range(len(prefix_sum)):
            # Check if we can form a valid subarray by removing elements from the front
            while deque_indices and prefix_sum[i] - prefix_sum[deque_indices[0]] >= K:
                min_length = min(min_length, i - deque_indices.popleft())
            
            # Maintain the deque in increasing order of prefix_sum
            while deque_indices and prefix_sum[i] <= prefix_sum[deque_indices[-1]]:
                deque_indices.pop()
            
            # Add the current index to the deque
            deque_indices.append(i)
        
        return min_length if min_length != float('inf') else -1
