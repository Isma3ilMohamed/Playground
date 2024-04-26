class Solution:
    def minFallingPathSum(self, arr):
        n = len(arr)
        if n == 1:
            return min(arr[0])

        # Initialize dp with the first row of arr
        dp = arr[0][:]

        for i in range(1, n):
            # Find the minimum and second minimum in the current dp
            min1, min2 = float('inf'), float('inf')
            for j in range(n):
                if dp[j] < min1:
                    min2 = min1
                    min1 = dp[j]
                elif dp[j] < min2:
                    min2 = dp[j]

            # Create a new list to store the current row values
            new_dp = [0] * n
            for j in range(n):
                if dp[j] == min1:
                    new_dp[j] = arr[i][j] + min2  # If dp[j] was the minimum, use the second minimum
                else:
                    new_dp[j] = arr[i][j] + min1  # Otherwise, use the minimum

            # Update dp to new_dp
            dp = new_dp

        # The answer is the minimum value in dp
        return min(dp)
