class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        # Step 1: Find the maximum possible OR value by ORing all elements
        max_or = 0
        for num in nums:
            max_or |= num
        
        # Initialize the count of subsets that have the maximum OR
        count = 0
        
        # Step 2: Define a recursive function to explore all subsets
        def dfs(i, current_or):
            nonlocal count
            # If we have processed all elements, check the OR value
            if i == len(nums):
                if current_or == max_or:
                    count += 1
                return
            
            # Case 1: Include the current number in the subset
            dfs(i + 1, current_or | nums[i])
            
            # Case 2: Exclude the current number from the subset
            dfs(i + 1, current_or)
        
        # Start the recursive process from index 0 with an OR value of 0
        dfs(0, 0)
        
        return count
