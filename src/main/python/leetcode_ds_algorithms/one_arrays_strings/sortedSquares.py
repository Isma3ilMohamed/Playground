from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted(x*x for x in nums)
        numArr = []
        for x in nums:
            numArr.append(x * x)
        numArr.sort()
        return numArr
