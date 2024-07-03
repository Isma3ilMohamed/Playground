
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        n = len(nums)

        # Calculate the minimum difference for all scenarios
        return min(
            nums[n-4] - nums[0],  # Remove three smallest elements
            nums[n-1] - nums[3],  # Remove three largest elements
            nums[n-3] - nums[1],  # Remove two smallest and one largest element
            nums[n-2] - nums[2]   # Remove one smallest and two largest elements
        )
