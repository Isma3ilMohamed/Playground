from typing import List
import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort the intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Initialize a min-heap to track end times
        heap = []
        
        for interval in intervals:
            start, end = interval
            if heap and start > heap[0]:
                # Reuse the group (pop the earliest ending interval)
                heapq.heappop(heap)
            # Assign the interval to a new or existing group
            heapq.heappush(heap, end)
        
        # The number of groups is the size of the heap
        return len(heap)
