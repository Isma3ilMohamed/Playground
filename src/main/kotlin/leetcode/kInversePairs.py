class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        prev = [0] * (k + 1)
        prev[0] = 1

        for N in range(1, n + 1):
            curr = [0] * (k + 1)
            total = 0  # sliding window
            for k in range(0, k + 1):
                if k >= N:
                    total -= prev[k - N]
                total = (total + prev[k]) % MOD
                curr[k] = total

            prev = curr
        return prev[k]


solve = Solution()
print(solve.kInversePairs(3, 0))
