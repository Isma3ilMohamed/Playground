class Solution:
    def findLHS(self, nums: List[int]) -> int:
        map = {}
        res = 0
        for num in nums:
            map[num] = map.get(num, 0) + 1
            if map.__contains__(num + 1):
                res = max(res, map.get(num) + map.get(num + 1))
            if map.__contains__(num - 1):
                res = max(res, map.get(num) + map.get(num - 1))
        return res
