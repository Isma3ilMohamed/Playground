from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dictionary_set = set(dictionary)
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 0  # Empty string has zero extra characters

        for i in range(1, n + 1):
            # Assume the current character is extra
            dp[i] = dp[i - 1] + 1
            # Check all possible prefixes ending at position i
            for j in range(0, i):
                if s[j:i] in dictionary_set:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
