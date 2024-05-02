class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ans = -1

        # A set to store seen numbers
        seen = set()

        for num in nums:
            abs_num = abs(num)

            # If the absolute value is greater than the current maximum and its negation is seen
            if abs_num > ans and -num in seen:
                ans = abs_num
            seen.add(num)  # Insert the current number into the set

        return ans


s = Solution()
print(s.findMaxK(nums=[-10, 8, 6, 7, -2, -3]))
