class Solution:

    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        increasing, idx, nums_len = [], 0, len(nums)
        for i, (num1, num2) in enumerate(pairwise(nums)):
            if num1 >= num2:
                if i - idx >= k - 1:
                    increasing.append((idx, i))
                idx = i + 1
        if nums_len - 1 - idx >= k - 1:
            increasing.append((idx, nums_len - 1))

        for a, b in increasing:
            if b - a + 1 >= 2 * k:
                return True

        for (_, b1), (a2, _) in pairwise(increasing):
            if a2 == b1 + 1:
                return True
        else:
            return False
