class Solution:
    def rob(self, nums: list[int]) -> int:
        rob, no_rob = 0, 0
        for num in nums:
            new_rob, new_no_rob = no_rob + num, max(no_rob, rob)
            rob, no_rob = new_rob, new_no_rob
        return max(rob, no_rob)
