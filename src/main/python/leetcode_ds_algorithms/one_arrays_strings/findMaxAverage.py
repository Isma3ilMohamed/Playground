class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if len(nums) <= 1:
            return nums[0] / k
        curr = 0
        for i in range(k):
            curr += nums[i]
        ans = curr / k
        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            ans = max(ans, curr / k)
        return ans
