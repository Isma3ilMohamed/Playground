class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            # Compare between the current and the next number
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        return True
