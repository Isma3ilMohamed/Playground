import heapq
from typing import List

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Initialize the min-heap
        heap = []
        max_value = float('-inf')
        
        # Build initial heap and find the initial max_value
        for i in range(len(nums)):
            value = nums[i][0]
            heapq.heappush(heap, (value, i, 0))  # (value, list_index, element_index)
            max_value = max(max_value, value)
        
        # Initialize the range
        min_range = [float('-inf'), float('inf')]
        
        while heap:
            min_value, list_idx, elem_idx = heapq.heappop(heap)
            # Update the range if it's smaller
            if max_value - min_value < min_range[1] - min_range[0]:
                min_range = [min_value, max_value]
            elif max_value - min_value == min_range[1] - min_range[0] and min_value < min_range[0]:
                min_range = [min_value, max_value]
            
            # If there is a next element in the same list, add it to the heap
            if elem_idx + 1 < len(nums[list_idx]):
                next_value = nums[list_idx][elem_idx + 1]
                heapq.heappush(heap, (next_value, list_idx, elem_idx + 1))
                max_value = max(max_value, next_value)
            else:
                # One of the lists is exhausted
                break
        
        return min_range
