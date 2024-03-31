class Solution:

    # def findDuplicates(self, nums: List[int]) -> List[int]:
    #     return [num for num,freq in Counter(nums).items() if freq >= 2]
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for n in nums:
            n = abs(n)

            if nums[n-1] < 0:
                res.append(n)
            nums[n-1] = -nums[n-1]

        return res


solution = Solution()
print(solution.findDuplicates(nums=[4,3,2,7,8,2,3,1]))