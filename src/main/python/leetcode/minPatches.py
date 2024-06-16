class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1
        patches = 0
        i = 0
        
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                # If the current number can contribute to the sum, use it
                miss += nums[i]
                i += 1
            else:
                # Patch the array with the smallest missing number
                miss += miss
                patches += 1
        
        return patches
