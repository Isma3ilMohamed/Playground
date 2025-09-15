class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        dic = Counter(nums)
        res = len(nums)//2
        for key,  value in dic.items():
            if key==target and value > res:
                return True
        return False
