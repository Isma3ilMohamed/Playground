from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        # Sort the array to ensure sequences are checked in ascending order
        nums.sort()
        
        # Convert the list to a set for O(1) lookup
        num_set = set(nums)
        max_streak = 0
        
        # Iterate through each number in sorted order to start a new sequence
        for num in nums:
            # Start a sequence only if it's the smallest element in that sequence
            current_streak = 0
            current_num = num
            
            # Check if each successive square exists in the set
            while current_num in num_set:
                current_streak += 1
                current_num = current_num ** 2
            
            # Update the maximum streak found
            max_streak = max(max_streak, current_streak)
        
        # Return max_streak if it's greater than 1, else return -1
        return max_streak if max_streak > 1 else -1
