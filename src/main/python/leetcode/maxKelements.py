import heapq
import math
from typing import List

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # Initialize max heap with negative values
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        
        score = 0
        for _ in range(k):
            # Pop the largest element
            largest = -heapq.heappop(max_heap)
            score += largest
            # Compute the new value using ceil division
            new_value = math.ceil(largest / 3)
            # Push the new value back into the heap
            heapq.heappush(max_heap, -new_value)
        
        return score
