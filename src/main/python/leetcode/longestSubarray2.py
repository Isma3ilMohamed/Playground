class Solution:
    def longestSubarray2(self, nums: List[int]) -> int:
        max_num = max(nums)          # Step 1: Find the maximum element
        max_len = 0
        current_len = 0

        for num in nums:             # Step 3: Iterate through the array
            if num == max_num:
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                current_len = 0

        return max_len               # Step 4: Return the result
