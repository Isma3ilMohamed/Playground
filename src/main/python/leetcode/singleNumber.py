class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for n in nums:
            if n in ans:
                ans.remove(n)
            else:
                ans.add(n)
        return list(ans)
