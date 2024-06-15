class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Combine the profits and capital into a list of tuples and sort them by capital
        projects = sorted(zip(capital, profits))
        
        max_heap = []
        current = 0
        
        for _ in range(k):
            # Push all projects that can be undertaken with the current capital to the max-heap
            while current < len(projects) and projects[current][0] <= w:
                # We push negative profit because Python's heapq is a min-heap by default
                heapq.heappush(max_heap, -projects[current][1])
                current += 1
            
            # If the max-heap is empty, no more projects can be undertaken
            if not max_heap:
                break
            
            # Pop the most profitable project from the max-heap
            w -= heapq.heappop(max_heap)
        
        return w
