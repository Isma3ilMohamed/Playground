class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = []
        
        # Initialize the heap with the first k elements of nums
        for num in nums:
            self.add(num)
    
    def add(self, val: int) -> int:
        # Add the new element to the heap
        heapq.heappush(self.min_heap, val)
        
        # If the heap exceeds size k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
        
        # The root of the heap is the k-th largest element
        return self.min_heap[0]
