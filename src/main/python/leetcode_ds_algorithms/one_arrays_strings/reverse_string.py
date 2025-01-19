from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Don't return anything, modify s in-place instead
        """
        swap = ""
        l = 0
        r = len(s) - 1
        while l < r:
            swap = s[l]
            s[l] = s[r]
            s[r] = swap
            l += 1
            r -= 1
