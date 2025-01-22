class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i in range(len(nums)):
            if seen.__contains__(nums[i]):
                return True
            seen.add(nums[i])
            if len(seen) > k:
                seen.remove(nums[i - k])
        return False
