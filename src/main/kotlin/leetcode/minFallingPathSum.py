class Solution:
    def minFallingPathSum(self, matrix: list[list[int]]) -> int:
        N = len(matrix)
        cache = {}

        def dfs(r, c):
            if r == N:
                return 0
            if c < 0 or c == N:
                return float("inf")
            if (r, c) in cache:
                return cache[(r, c)]
            res = matrix[r][c] + min(
                dfs(r + 1, c - 1),
                dfs(r + 1, c),
                dfs(r + 1, c + 1),
            )
            cache[(r, c)] = res
            return res

        res = float("inf")
        for c in range(N):
            res = min(res, dfs(0, c))
        return res


solution = Solution()
print(solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]]))
