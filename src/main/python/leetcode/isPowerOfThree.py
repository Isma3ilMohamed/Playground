class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        max_int = (2**32 // 2) - 1
        max_n = 3 ** floor(log(max_int, 3))

        return n > 0 and max_n % n == 0
