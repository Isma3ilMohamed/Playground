class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2

        existing = set()

        for num in nums:
            for n in list(existing):
                if n+num <= target:existing.add(n+num)
            existing.add(num)
            if target in existing:return True
        
        return False


        

        
