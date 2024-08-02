class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        
        # Double the array to handle the circular nature
        extended_nums = nums + nums
        
        max_ones_in_window = 0
        current_ones_in_window = 0
        
        # Initialize the first window
        for i in range(total_ones):
            current_ones_in_window += extended_nums[i]
        
        max_ones_in_window = current_ones_in_window
        
        # Slide the window across the extended array
        for i in range(total_ones, len(extended_nums)):
            current_ones_in_window += extended_nums[i] - extended_nums[i - total_ones]
            max_ones_in_window = max(max_ones_in_window, current_ones_in_window)
        
        return total_ones - max_ones_in_window
