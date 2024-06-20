class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions
        position.sort()
        
        # Helper function to determine if we can place m balls with at least min_dist apart
        def canPlaceBalls(min_dist: int) -> bool:
            count = 1  # Place the first ball at the first position
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= min_dist:
                    count += 1
                    last_position = position[i]
                if count >= m:
                    return True
            return False
        
        # Binary search for the maximum minimum distance
        low, high = 1, position[-1] - position[0]
        
        while low < high:
            mid = (low + high + 1) // 2
            if canPlaceBalls(mid):
                low = mid  # Try for a larger distance
            else:
                high = mid - 1  # Try for a smaller distance
        
        return low
