class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        
        # dp[i][j] will store the minimum number of operations to print s[i:j+1]
        dp = [[0] * n for _ in range(n)]
        
        # Fill the dp table
        for length in range(1, n + 1):  # length of the substring
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = length  # worst case (print each character separately)
                for k in range(i, j):
                    if s[k] == s[j]:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j - 1])
                    else:
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])
        
        return dp[0][n - 1]
