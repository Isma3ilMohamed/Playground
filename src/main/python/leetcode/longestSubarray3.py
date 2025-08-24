class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans = zeros = left = 0
        for i in range(len(nums)):
            zeros += nums[i] == 0
            while zeros > 1:
                zeros -= nums[left] == 0
                left += 1
            ans = max(ans, i - left)
        return ans
