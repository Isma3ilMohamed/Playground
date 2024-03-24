class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)

        for key,item in counter.items():
            if item > 1:
                return key
        return 0
