class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counts = set()
        for val in nums:
            if val in counts:
                return val
            else:
                counts.add(val)
        return 0
