class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        max_area = 0
        heights = [0] * (len(matrix[0]) + 1)

        for row in matrix:
            for i in range(len(matrix[0])):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            # Compute the max area for the histogram created from the current row
            stack = []

            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
        return max_area


solution = Solution()
print(solution.maximalRectangle(matrix=[["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
                                        ["1", "0", "0", "1", "0"]]))
