class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Initialize min_val and max_val with the first array's first and last elements
        min_val, max_val = arrays[0][0], arrays[0][-1]
        max_distance = 0
        
        # Iterate through the rest of the arrays
        for i in range(1, len(arrays)):
            current_array = arrays[i]
            # Calculate potential max distance with the current array
            max_distance = max(max_distance, abs(current_array[-1] - min_val), abs(max_val - current_array[0]))
            
            # Update global min and max
            min_val = min(min_val, current_array[0])
            max_val = max(max_val, current_array[-1])
        
        return max_distance
