class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[val] for val in nums]
        res = []
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] % nums[i] == 0 and len(dp[j]) >= len(dp[i]):
                    dp[i] = [nums[i]] + dp[j]
            res = dp[i] if len(dp[i]) > len(res) else res
        return res
