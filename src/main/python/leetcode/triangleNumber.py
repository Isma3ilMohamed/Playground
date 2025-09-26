class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        l = len(nums)
        nums.sort()
        result = 0
        for i in range(l-1,1,-1):
            target = nums[i]
            m = 0
            n = i -1
            while m < n:
                if nums[m] + nums[n] <= target:
                    m += 1
                else:
                    result += n -m
                    n -= 1
        return result
