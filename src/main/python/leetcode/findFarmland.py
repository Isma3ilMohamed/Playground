from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        result = []

        def findRectangle(r, c):
            # Initial position, assume r, c is the start of a new rectangle
            end_col = c
            while end_col + 1 < cols and land[r][end_col + 1] == 1:
                end_col += 1
            
            end_row = r
            while end_row + 1 < rows and all(land[end_row + 1][col] == 1 for col in range(c, end_col + 1)):
                end_row += 1

            # Append the rectangle coordinates to the result list
            result.append([r, c, end_row, end_col])
            
            # Optionally mark the visited cells (this part is just to visualize if needed)
            for i in range(r, end_row + 1):
                for j in range(c, end_col + 1):
                    land[i][j] = 0

        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1:  # Start of a new rectangle
                    findRectangle(i, j)

        return result

# Example usage:
sol = Solution()
land_input = [
    [1, 0, 0],
    [0, 1, 1],
    [0, 1, 1]
]
print(sol.findFarmland(land_input))
