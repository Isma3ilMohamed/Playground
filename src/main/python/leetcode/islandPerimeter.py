class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:

                    neighbors = 0
                    if i > 0 and grid[i - 1][j] == 1:
                        neighbors += 1
                    if j > 0 and grid[i][j - 1] == 1:
                        neighbors += 1
                    if i < rows - 1 and grid[i + 1][j] == 1:
                        neighbors += 1
                    if j < cols - 1 and grid[i][j + 1] == 1:
                        neighbors += 1
                    perimeter += 4 - neighbors

        return perimeter
