class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        ans = [0] * n
        max_height = 0
        for i in range(n - 1, -1, -1):
            if max_height < height[i]:
                max_height = height[i]
            ans[i] = max_height

        max_height = 0
        sol = 0
        for i in range(n):
            if max_height < height[i]:
                max_height = height[i]
            sol += min(max_height, ans[i]) - height[i]

        return sol


solution = Solution()
print(solution.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
